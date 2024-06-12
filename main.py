from indexing.processing import process_pdf

file = process_pdf('/home/ahmed/Downloads/The Vital Question Energy, Evolution, and the Origins of Complex Life (Nick Lane) (Z-Library).pdf')
print(file.open_and_read_pdf()[:2])

