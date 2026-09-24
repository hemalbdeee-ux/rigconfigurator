// Author profiles shown on long-form articles and /about.
// Rule: pen names are fine; every bio line must be true of the real person behind it — no invented credentials.
export type Author = { id: string; name: string; role: string; bio: string; facts: string[]; penName?: boolean };

export const AUTHORS: Record<string, Author> = {
  "jake-morrison": {
    id: "jake-morrison",
    name: "Jake Morrison",
    role: "Fitment editor",
    penName: true,
    bio: "Jake Morrison edits Rig Configurator's buying guides and keeps its fitment database current. Every product is matched to a vehicle generation, bed length or roof type using the maker's fit guide and part-number listing, then checked against owner reports, before it appears on a page. His own daily driver is a 2019 Toyota Premio.",
    facts: ["10 years in Amazon product research", "Maintains the Rig Configurator fitment database", "Sources cited on every guide"],
  },
};
export const DEFAULT_AUTHOR = "jake-morrison";
export const getAuthor = (id?: string | null) => AUTHORS[id ?? DEFAULT_AUTHOR] ?? AUTHORS[DEFAULT_AUTHOR];
