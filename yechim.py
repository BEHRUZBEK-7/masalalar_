# # Yechim
# class Transport:
#     def __init__(self, model: str, yil: int) -> None:
#         self.model = model
#         self.yil = yil
#
#     def malumot(self) -> str:
#         return f"Model: {self.model}, Yil: {self.yil}"
#
#
# class Avtomobil(Transport):
#     def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, Yonilg'i: {self.yonilgi_turi}"
#
#
# class Avtobus(Transport):
#     def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
#         super().__init__(model, yil)
#         self.orinlar_soni = orinlar_soni
#
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, O'rinlar: {self.orinlar_soni}"
#
#
# a = Avtomobil("Cobalt", 2022, "benzin")
# print(a.malumot())
#
# b = Avtobus("Isuzu", 2018, 40)
# print(b.malumot())
#
# #2-masala
# class Kitob:
#     def __init__(self, nom, mualif, yil) -> None:
#         self.nom = nom
#         self.yil = yil
#         self.mualif = mualif
#
#     def taqdimot(self) -> str:
#         return f"tadimot"
# class Elektronkitonlar(Kitob):
#     def __init__(self,nom, muallif, yil) -> None:
#         super().__init__(nom, muallif, yil)
#     def taqdimot(self) -> str:
#         return f"taqdimot"
# class Audikitob(Kitob):
#     def __init__(self,nom, mualif, yil) -> None:
#         super().__init__(nom, mualif, yil)
#
# e = Elektronkitonlar("Python asoslari", "Ali", 2023, 5)
# a = Audikitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)
#
# print(e.taqdimot())
# print(a.taqdimot())

#3-masala
# class Xodim :
#     def __init__(self, ism, mosh):
#         self.ism = ism
#         self.mosh = mosh
#
# class Manager(Xodim):
#     def __init__(self, ism, mosh):
#         Xodim.__init__(self, ism, mosh)
#
#     Manager = Xodim("Farhod",12000 )
# print(Manager.ism)
# print(Manager.mosh)


#4-masala
# class Xodim:
#     def __init__(self, ism, asosy_maosh):
#         self.ism = ism
#         self.asosy_maosh = asosy_maosh
#     def oylik(self):
#         return self.asosy_maosh
#     def malumot(self):
#         return f"Ism: {self.ism}, asosy maosh: {self.asosy_maosh}"
# class Oqsoch(Xodim):
#     def __init__(self, ism, asosy_maosh, bonus_foiz):
#         super().__init__(ism, asosy_maosh)
#         self.bonus_foiz = bonus_foiz
#     def oylik(self):
#         bonus = self.bonus_foiz * (self.bonus_foiz / 100)
#         return self.asosy_maosh + bonus
# class SoatbayXodim(Xodim):
#     def __init__(self, ism, soat, soatlik_stavka):
#         maosh = soat * soatlik_stavka
#         super().__init__(ism, maosh)
#         self.soat = soat
#         self.soatlik_stavka = soatlik_stavka
# o = Oqsoch("Dilshod", 5_000_000, 20)
# s = SoatbayXodim("Aziza", 160, 50_000)
#
# print(o.malumot())
# print(s.malumot())