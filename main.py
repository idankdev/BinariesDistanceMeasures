from sample import Sample
from scanner import Scanner

def main():
    scanner = Scanner()
    db = scanner.db
    db.AddSample(Sample("/bin/cat", "cat"))
    db.AddSample(Sample("/bin/ls", "ls"))
    db.AddSample(Sample("/usr/bin/whoami", "whoami"))
    db.AddSample(Sample("/usr/bin/head", "head"))

    sample = Sample("/usr/bin/tail", "tail")

    scanner.FindClosestStringsSample(sample)
    scanner.FindClosetTextSample(sample)
    scanner.FindClosestFileSample(sample)


if __name__ == '__main__':
    main()