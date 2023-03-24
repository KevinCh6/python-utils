# -*- coding:UTF-8 -*-
# DATE: 2023/03/24
# TIME: 9:42

# DESCRIPTION:
import pdfplumber


class PdfTransfer(object):
    def __init__(self):
        pass

    @staticmethod
    def read_pdf(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                yield page.extract_text()
                page.flush_cache()

    @staticmethod
    def parse(pdf_path, txt_path):
        """

        :param pdf_path:
        :param txt_path:
        :return:
        """
        with open(txt_path, 'w') as ot:
            for page_content in PdfTransfer.read_pdf(pdf_path):
                lines = str(page_content).split('\n')
                for line in lines:
                    ot.write(line + '\n')


if __name__ == '__main__':
    pdf = './exm/exm.pdf'
    txt = './exm/exm.pdf.txt'
    PdfTransfer.parse(pdf, txt)
