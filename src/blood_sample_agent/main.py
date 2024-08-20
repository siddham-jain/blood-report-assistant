from pypdf import PdfReader
import argparse
from crew import create_crew

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    number_of_pages = len(reader.pages)

    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text = page.extract_text()

    return text

def main():
    parser = argparse.ArgumentParser(description='Summarize and provide health recommendations based on blood sample data')
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file")
    args = parser.parse_args()
    if args.pdf_path:
        print(f"PDF path provided: {args.pdf_path}")
    else:
        print("Error: No PDF path provided. Please specify the path to the PDF file.")

    text = extract_text_from_pdf(args.pdf_path)

    crew = create_crew(text)
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()



