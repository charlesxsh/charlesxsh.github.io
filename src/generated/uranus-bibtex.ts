export default [
    {
        "name": "Who Goes First? Detecting Go Concurrency Bugs via Message Reordering",
        "authors": [
            {
                "name": "Ziheng Liu*"
            },
            {
                "name": "Shihao Xia*"
            },
            {
                "name": "Yu Liang"
            },
            {
                "name": "Linhai Song"
            },
            {
                "name": "Hong Hu"
            }
        ],
        "authorExtra": "",
        "publicAt": "Proceedings of the 27th International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS 2022)",
        "abstract": "Go is a young programming language invented to build safe and efficient concurrent programs. It provides goroutines as lightweight threads and channels for inter-goroutine communication. Programmers are encouraged to explicitly pass messages through channels to connect goroutines, with the purpose of reducing the chance of making programming mistakes and introducing concurrency bugs. Go is one of the most beloved programming languages and has already been used to build many critical infrastructure software systems in the data-center environment. However, a recent study shows that channel-related concurrency bugs are still common in Go programs, severely hurting the reliability of Go applications.\nThis paper presents GFuzz, a dynamic detector that can effectively pinpoint channel-related concurrency bugs by mutating the processing orders of concurrent messages. We build GFuzz in three steps. We first adopt an effective approach to identify concurrent messages and transform a program to process those messages in any given order. We then take a fuzzing approach to generate new processing orders by mutating exercised ones and rely on execution feedback to prioritize orders close to triggering bugs. Finally, we design a runtime sanitizer to capture triggered bugs that are missed by the Go runtime. We evaluate GFuzz on seven popular Go software systems, including Docker, Kubernetes, and gRPC. GFuzz finds 184 previously unknown bugs and reports a negligible number of false positives. Programmers have already confirmed 124 reports as real bugs and fixed 67 of them based on our reporting. A careful inspection of the detected concurrency bugs from gRPC shows the effectiveness of each component of GFuzz and confirms the components\u2019 rationality.\n",
        "paperLink": "/assets/bibtex/liu:gfuzz.pdf",
        "month": "February--March",
        "year": "2022",
        "githubLink": "https://github.com/system-pclub/GFuzz",
        "githubStarsSvgLink": "https://img.shields.io/github/stars/system-pclub/GFuzz.svg?style=social&label=Star&maxAge=2592000",
        "slideLink": "/assets/bibtex/liu:gfuzz-slides.pdf",
        "bibtex": "@inproceedings{liu:gfuzz,\n address = {Lausanne, Switzerland},\n author = {Ziheng Liu* and Shihao Xia* and Yu Liang and Linhai Song and Hong Hu},\n booktitle = {Proceedings of the 27th International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS 2022)},\n month = {February--March},\n title = {{Who Goes First? Detecting Go Concurrency Bugs via Message Reordering}},\n www-url = {https://github.com/system-pclub/GFuzz},\n year = {2022}\n}\n\n"
    }
]