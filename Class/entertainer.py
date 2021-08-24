class Entertainer:
    def __init__(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height
    def set_face(self, face):
        self.face = face
    def set_kind(self, kind):
        self.kind = kind
    def set_name(self, name):
         self.name = name
    # def info(self):
    #     print(f"이름: {self.name}\t 키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}")
    def __str__(self):
        return f"이름: {self.name}\t 키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}"

아이유 = Entertainer('아이유');
# 아이유.set_name('이지은')
아이유.set_height('161cm')
아이유.set_face('형섭쌤이상형')
아이유.set_kind("that's very good")
print(아이유)
# 아이유.info()
class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def __str__(self):
        return  super().__str__()+f"\t대표노래: {self.song}"

신우 = Singer('신동우', '걸어본다')
신우.set_height('182cm')
신우.set_face('멋짐')
신우.set_kind('착함')
print(신우)

김동률 = Singer('김동률', '출발')
김동률.set_height(175)
김동률.set_face('평범')
김동률.set_kind('good')
print(김동률)

class Talent(Entertainer):
    def __init__(self, name, drama):
        super().__init__(name)
        self.drama = drama

    def __str__(self):
        return super().__str__()+f"" \
                                 f"\t드라마: {self.drama}"

송중기 = Talent("송중기", "태양의 후예")
송중기.set_height("178cm")
송중기.set_face("잘생김")
송중기.set_kind('착하다')
print(송중기)

뷔 = Singer('뷔', 'Love Maze')
뷔.set_height('179cm')
뷔.set_face('진이지 이상형')
뷔.set_kind('That\'s very good and cute.')
print(뷔)

RM = Singer('RM', 'Answer: love myself')
RM.set_height('179cm')
RM.set_face('쏘쏘')
RM.set_kind('자기철학이 있어보임')
print(RM)

방탄소년단 = []
방탄소년단.append(뷔)
방탄소년단.append(RM)
print(방탄소년단)
