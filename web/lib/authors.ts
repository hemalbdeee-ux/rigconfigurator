// Author profiles shown on long-form articles and /about. Keep every line factual — no invented credentials.
export type Author = { id: string; name: string; role: string; bio: string; facts: string[] };

export const AUTHORS: Record<string, Author> = {
  "md-hanzala": {
    id: "md-hanzala",
    name: "Md Hanzala",
    role: "Founder & fitment editor",
    bio: "Md Hanzala runs Rig Configurator and maintains its fitment database: every product is matched to a vehicle generation from manufacturer fit guides, part-number listings and owner reports before it appears on a page.",
    facts: ["10 years in Amazon product research", "Maintains the Rig Configurator fitment database", "Sources cited on every guide"],
  },
};
export const getAuthor = (id?: string | null) => AUTHORS[id ?? "md-hanzala"] ?? AUTHORS["md-hanzala"];
