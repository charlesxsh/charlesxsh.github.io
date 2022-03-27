export interface Author {
    name: string
    link?: string
}

export interface Paper {
    name: string;
    authors?: Author[];
    authorExtra?: string;
    publicAt?: string;
    abstract?: string;
    paperLink?: string;
    githubLink?: string;
    githubStarsSvgLink?: string;
    slideLink?: string;
    bibtex?: string;
    year?: string;
    month?: string;
}