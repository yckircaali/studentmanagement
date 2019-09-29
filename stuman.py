class Exam(object):
    def __init__(self,dogru_sayisi,yanlis_sayisi,note):
    	self.score = []
		for count in range(number):
		self.score.append(0)

        self.dogru_sayisi = dogru_sayisi
        self.yanlis_sayisi = yanlis_sayisi
        self.note = note

    def score(self):
        puanlar = (100 / (int(self.dogru) + int(self.yanlis)))
        self.puan = puanlar
        return self.puan

class Student(object):
    def __init__(self, ogrenci_adi, sinavlar):
        self.ogrenci_adi = ogrenci_adi
        self.sinavlar = sinavlar

    def ogrenci_adi(self):
		return self.ogrenci_adi

	def avg_score(self):
    	return sum(self.score) / len(self._score)
   
class Sinif(object):
    def __init__(self,sinif_listesi,sinif_ort)
        self.sinif_listesi = sinif_listesi
        self.sinif_ort = sinif_ort

    def class_avg(self):
    	return sum(self.score) / len(self.score)
        
        
