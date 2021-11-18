class Score:
    def __init__(self, n, k=0, e=0, m=0):
        self.name = n
        self.kor = k
        self.eng = e
        self.mat = m

    def avg(self):
        return (self.kor + self.eng +self.mat) / 3

    def __str__(self):
        return f"이름:{self.name} 국어:{self.kor} 영어:{self.eng} 수학:{self.mat} 평균:{self.avg():0.2f}"

    def file_content(self):
        f"{self.name},{self.kor},{self.eng},{self.mat}\n"


if __name__ == "__main__":
    s1 = Score("김인하", 100, 90, 80)
    s2 = Score("김민하", 90, 50, 20)
    
    def avg(k, e, m):
        return (k+e+m)/3
    
    print(avg(s1.kor + s1.eng + s1.mat))
    print(avg(s2.kor + s2.eng + s1.mat))
    
    print(s1.avg())
    print(s2.avg())