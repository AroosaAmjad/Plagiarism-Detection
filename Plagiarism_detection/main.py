from difflib import SequenceMatcher

with open('D:\Python\Plagiarism_detection\Demo1.txt') as one_file, open('D:\Python\Plagiarism_detection\Demo2.txt') as two_file:
    data_file1 = one_file.read()
    data_file2 = two_file.read()
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f"The plagiarized content is {matches}%")


