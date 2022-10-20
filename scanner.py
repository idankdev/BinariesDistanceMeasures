from sample import Sample
from db import DB


class Scanner():
    def __init__(self):
        self.db = DB()

    def CompareStrings(self, sample1: Sample, sample2: Sample) -> tuple:
        """
        Compares the strings of two samples
        :param sample1: Sample object
        :param sample2: Sample object
        :return distance, list of strings that are common to both samples: tuple
        """
        mutual = 0
        mutual_strings = []
        for string1 in sample1.strings:
            if string1 in sample2.strings:
                mutual += 1
                mutual_strings.append(string1)
        return round(2 * mutual / (len(sample1.strings) + len(sample2.strings)) * 100, 2), mutual_strings

    def CountMutualTextHashes(self, sample1: Sample, sample2: Sample) -> int:
        """
        Counts the number of mutual hashes of the .text section of two samples.
        Locates different block between the two samples.
        :param sample1: Sample object
        :param sample2: Sample object
        :return: int
        """
        mutual = 0
        for i in range(min(len(sample1.text_hash_blocks), len(sample2.text_hash_blocks))):
            if sample1.text_hash_blocks[i] != sample2.text_hash_blocks[i]:
                return mutual
            mutual += 1
        return mutual

    def CountMutualFileHashes(self, sample1: Sample, sample2: Sample) -> int:
        """
        Counts the number of mutual hashes of the file of two samples.
        Locates different block between the two samples.
        :param sample1: Sample object
        :param sample2: Sample object
        :return: int
        """
        mutual = 0
        for i in range(min(len(sample1.file_hash_blocks), len(sample2.file_hash_blocks))):
            if sample1.file_hash_blocks[i] != sample2.file_hash_blocks[i]:
                return mutual
            mutual += 1
        return mutual

    def FindClosestStringsSample(self, sample: Sample) -> bool:
        """
        Finds the sample with the closest strings to the given sample.
        :param sample: Sample object
        :return: bool
        """
        max_distance = 0
        max_distance_sample = None
        for sample in self.db.db:
            distance, _ = self.CompareStrings(sample, sample)
            if distance > max_distance:
                max_distance = distance
                max_distance_sample = sample
        if max_distance_sample is not None:
            print(
                f"Found sample with the closest strings:\nName:\t{max_distance_sample.name}\nOriginal path:\t{max_distance_sample.original_path}\nDistance:\t{max_distance}")
            return True
        return False

    def FindClosetTextSample(self, sample: Sample) -> bool:
        """
        Finds the sample with the closest .text section to the given sample.
        :param sample: Sample object
        :return: bool
        """
        min_mutual = 0
        min_mutual_sample = None
        for sample in self.db.db:
            mutual = self.CountMutualTextHashes(sample, sample)
            if mutual > min_mutual:
                min_mutual = mutual
                min_mutual_sample = sample
        if min_mutual_sample is not None:
            print(
                f"Found sample with the closest .text section:\nName:\t{min_mutual_sample.name}\nOriginal path:\t{min_mutual_sample.original_path}\nMutual hashes:\t{min_mutual}")
            return True
        return False

    def FindClosestFileSample(self, sample: Sample) -> bool:
        """
        Finds the sample with the closest file to the given sample.
        :param sample: Sample object
        :return: bool
        """
        min_mutual = 0
        min_mutual_sample = None
        for sample in self.db.db:
            mutual = self.CountMutualFileHashes(sample, sample)
            if mutual > min_mutual:
                min_mutual = mutual
                min_mutual_sample = sample
        if min_mutual_sample is not None:
            print(
                f"Found sample with the closest file:\nName:\t{min_mutual_sample.name}\nOriginal path:\t{min_mutual_sample.original_path}\nMutual hashes:\t{min_mutual}")
            return True
        return False
