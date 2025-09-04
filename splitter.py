from sentiment_analysis import score_paragraph
import multitasking

@multitasking.task
def read(chunk_data,index):
    out = score_paragraph(chunk_data)
    print("Processing ==> ",index)
    return out


if __name__ == "__main__":
    with open("randomparas.txt", "r", encoding="utf-8") as f:
        huge_text = f.read()

    chunks = huge_text.split("\n") # splitting the huge text to paragraphs
    for i, chunk in enumerate(chunks):
        read(chunk,i)
    multitasking.wait_for_tasks()
    #f.close() # clearing memory leaks