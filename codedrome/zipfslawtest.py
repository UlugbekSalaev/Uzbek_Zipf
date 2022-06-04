import zipfslaw

def main():
    try:
        f = open("Oʻtgan kunlar.txt", "r", encoding="ansi")
        text = f.read()
        f.close()

        zipf_table = zipfslaw.generate_zipf_table(text, 1000)

        zipfslaw.print_zipf_table(zipf_table)

    except IOError as e:
        print(e)

main()
