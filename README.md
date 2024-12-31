# CHIE
CHIE: Generative MRC Evaluation for in-context QA with Correctness, Helpfulness, Irrelevancy, and Extraneousness Aspects

This repository collect the source code and some data from "CHIE: Generative MRC Evaluation for in-context QA with Correctness, Helpfulness, Irrelevancy, and Extraneousness Aspects".

Use CHIE: [WangChanX Eval](https://github.com/vistec-AI/WangchanX-Eval)

## Abstract

The evaluation of generative models in Machine Reading Comprehension (MRC) presents distinct difficulties, as traditional metrics like BLEU, ROUGE, METEOR, Exact Match, and F1 score often struggle to capture the nuanced and diverse responses. While embedding-based metrics such as BERTScore and BARTScore focus on semantic similarity, they still fail to fully address aspects such as recognizing additional helpful information and rewarding contextual faithfulness. Recent advances in large language model (LLM) based metrics offer more fine-grained evaluations, but challenges such as score clustering remain. This paper introduces a multi-aspect evaluation framework, CHIE,incorporating aspects of Correctness, Helpfulness, Irrelevance, and Extraneousness. Our approach, which uses binary categorical values rather than continuous rating scales, aligns well with human judgments, indicating its potential as a comprehensive and effective evaluation method.

Paper: [https://aclanthology.org/2024.genbench-1.10/](https://aclanthology.org/2024.genbench-1.10/)


## Citations

If you use CHIE in your project or publication, please cite the library as follows

```tex
@inproceedings{phatthiyaphaibun-etal-2024-chie,
    title = "{CHIE}: Generative {MRC} Evaluation for in-context {QA} with Correctness, Helpfulness, Irrelevancy, and Extraneousness Aspects",
    author = "Phatthiyaphaibun, Wannaphong  and
      Nonesung, Surapon  and
      Limkonchotiwat, Peerat  and
      Udomcharoenchaikit, Can  and
      Sawatphol, Jitkapat  and
      Chuangsuwanich, Ekapol  and
      Nutanong, Sarana",
    editor = "Hupkes, Dieuwke  and
      Dankers, Verna  and
      Batsuren, Khuyagbaatar  and
      Kazemnejad, Amirhossein  and
      Christodoulopoulos, Christos  and
      Giulianelli, Mario  and
      Cotterell, Ryan",
    booktitle = "Proceedings of the 2nd GenBench Workshop on Generalisation (Benchmarking) in NLP",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.genbench-1.10",
    pages = "154--164",
    abstract = "The evaluation of generative models in Machine Reading Comprehension (MRC) presents distinct difficulties, as traditional metrics like BLEU, ROUGE, METEOR, Exact Match, and F1 score often struggle to capture the nuanced and diverse responses. While embedding-based metrics such as BERTScore and BARTScore focus on semantic similarity, they still fail to fully address aspects such as recognizing additional helpful information and rewarding contextual faithfulness. Recent advances in large language model (LLM) based metrics offer more fine-grained evaluations, but challenges such as score clustering remain. This paper introduces a multi-aspect evaluation framework, CHIE,incorporating aspects of \textbf{C}orrectness, \textbf{H}elpfulness, \textbf{I}rrelevance, and \textbf{E}xtraneousness. Our approach, which uses binary categorical values rather than continuous rating scales, aligns well with human judgments, indicating its potential as a comprehensive and effective evaluation method.",
}
```
