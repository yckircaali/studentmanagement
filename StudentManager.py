class Exam():
    def __init__(self,DOGRU,YANLIS,SCORE):
        self.dogru = DOGRU
        self.yanlis = YANLIS
        self.score = SCORE
        self.toplam = 0

    def score(self,DOGRU,YANLIS,SCORE):
        score = (DOGRU * (100 / (DOGRU + YANLIS)))
        return self.score()

class Student():
    def __init__(self,OGRENCI_ADI,EXAM):
        self.ogrenci_adi = OGRENCI_ADI
        self.exam = EXAM

    def avg_score(self):
        return sum(self.score) / len(self._score)

class Class():
    def __init__(self):
        self.ogrenciler = list()  # ÖĞRENCİ LİSTESİ

    def ogrenciekle(self,OGRENCI_ADI,ISIM):
        self.ogrenciler.append(Student(OGRENCI_ADI,ISIM))  # ÖĞRENCİ EKLEMEK

    def class_avg(self):
            return sum(self.score) / len(self.score)