#https://github.com/patrickmineault/zipf
#https://github.com/UlugbekSalaev/Uzbek_Zipf

#https://goodresearch.dev/zipf.html
#https://iq.opengenus.org/zipfs-law/
#https://towardsdatascience.com/another-twitter-sentiment-analysis-with-python-part-3-zipfs-law-data-visualisation-fc9eadda71e7 [negative&positve tweets tokens]
#https://medium.com/@tigran.baseyan/%D0%B7%D0%B0%D0%BA%D0%BE%D0%BD-%D1%86%D0%B8%D0%BF%D1%84%D0%B0-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%B7%D0%B0%D0%BA%D0%BE%D0%BD-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B3%D0%BE-%D1%86%D0%B8%D0%BF%D1%84%D0%B0-975155b1cd03
# top 100ta suz butun matnni 37%ni tashkil qiladi

#https://www.analytics-tuts.com/zipfs-law-introduction-text-analytics/
#https://www.researchgate.net/publication/281896317_Large-Scale_Analysis_of_Zipf's_Law_in_English_Texts

import argparse
import pandas as pd
import pathlib

from zipf.parse_text import count_words
from zipf.fit_distribution import compute_summary

def main(args):
    # Process all text files.
    print(args)
    print(args.in_folder)
    paths = list(pathlib.Path(args.in_folder).glob("*.txt"))

    if not paths:
        raise Exception(f"No text files found in {args.in_folder}")

    # Create the paths if necessary
    out_path = pathlib.Path(args.out_folder)
    out_path.mkdir(exist_ok=True)
    (out_path / "raw_counts").mkdir(exist_ok=True)

    summaries = []
    for p in paths:
        print(p)
        with open(p, "r", encoding="ansi") as f:
            word_counts = count_words(f, False)

        df = pd.DataFrame(
            [
                {"word": x, "freq": y}
                for x, y in zip(word_counts.keys(), word_counts.values())
            ]
        )
        df = df.sort_values("freq", ascending=False)
        out_file = out_path / "raw_counts" / (p.stem + ".csv")
        df.to_csv(out_file)
        print(df)

        summary = compute_summary(word_counts)
        summary["name"] = p.stem
        summaries.append(summary)

    df = pd.DataFrame(summaries)
    df.set_index("name").to_csv(pathlib.Path(args.out_folder) / "summary.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute zipf distribution")
    parser.add_argument("--in_folder",  default="../data", help="the input folder")
    parser.add_argument("--out_folder", default="../results", help="the output folder")
    args = parser.parse_args()

    main(args)
