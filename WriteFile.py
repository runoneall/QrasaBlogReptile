def Write(FilePath:str, Content:str):
    with open(FilePath, 'w', encoding='utf-8') as File:
        File.write(Content)