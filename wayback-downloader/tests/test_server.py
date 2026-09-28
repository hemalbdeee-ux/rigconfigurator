import importlib
import time

from fastapi.testclient import TestClient

from .fake_archive import serve


def test_web_flow(tmp_path, monkeypatch):
    server, base = serve()
    monkeypatch.setenv("WAYBACK_BASE", base)
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    import wayback.archive

    importlib.reload(wayback.archive)
    import wayback.restore

    importlib.reload(wayback.restore)
    import wayback

    importlib.reload(wayback)
    import app.server as srv

    srv = importlib.reload(srv)
    c = TestClient(srv.app)
    try:
        assert "Restore any website" in c.get("/").text
        assert c.get("/api/snapshots", params={"url": "example.com"}).json()["snapshots"] == [
            "20150101000000", "20190101000000"
        ]
        assert c.post("/api/jobs", json={"url": "nope"}).status_code == 400
        assert c.post("/api/jobs", json={"url": "example.com", "timestamp": "2019-x"}).status_code == 400

        jid = c.post("/api/jobs", json={"url": "example.com", "timestamp": "2020"}).json()["id"]
        # an identical request joins the running job instead of starting another
        assert c.post("/api/jobs", json={"url": "example.com", "timestamp": "2020"}).json()["id"] == jid
        for _ in range(100):
            s = c.get(f"/api/jobs/{jid}").json()
            if s["stage"] in ("done", "error"):
                break
            time.sleep(0.1)
        assert s["stage"] == "done" and s["zip_ready"], s
        z = c.get(f"/api/jobs/{jid}/download")
        assert z.status_code == 200 and z.content[:2] == b"PK"
        page = c.get(f"/preview/{jid}/about/")
        assert page.status_code == 200 and "sandbox" in page.headers["content-security-policy"]
        assert c.get(f"/preview/{jid}/../manifest.json").status_code == 404
        assert c.get("/api/jobs/unknown").status_code == 404
    finally:
        server.shutdown()
