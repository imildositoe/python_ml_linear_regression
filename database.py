from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Float
from sqlalchemy.ext.declarative import declarative_base


#database connection
engine = create_engine('sqlite:///ml_db.sqlite', echo=True)
base = declarative_base()

class Train(base):
    __tablename__ = 'train'

    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

    def __init__(self, x, y1, y2, y3, y4):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

class Ideal(base):
    __tablename__ = 'ideal'

    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

    def __init__(self,x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25
                 ,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y40,y41,y42,y43,y44,y45,y46,y47,y48,y49,y50):
        self.x = x
        self.y1 = y1; self.y2 = y2; self.y3 = y3; self.y4 = y4; self.y5 = y5; self.y6 = y6; self.y7 = y7; self.y8 = y8; self.y9 = y9; self.y10 = y10
        self.y11 = y11; self.y12 = y12; self.y13 = y13; self.y14 = y14; self.y15 = y15; self.y16 = y16; self.y17 = y17; self.y18 = y18; self.y19 = y19; self.y20 = y20
        self.y21 = y21; self.y22 = y22; self.y23 = y23; self.y24 = y24; self.y25 = y25; self.y26 = y26; self.y27 = y27; self.y28 = y28; self.y29 = y29; self.y30 = y30
        self.y31 = y31; self.y32 = y32; self.y33 = y33; self.y34 = y34; self.y35 = y35; self.y36 = y36; self.y37 = y37; self.y38 = y38; self.y39 = y39; self.y40 = y40
        self.y41 = y41; self.y42 = y42; self.y43 = y43; self.y44 = y44; self.y45 = y45; self.y46 = y46; self.y47 = y47; self.y48 = y48; self.y49 = y49; self.y50 = y50
        
class Test(base):
    __tablename__ = 'test'

    x = Column(Float)
    y = Column(Float)
    delta_y = Column(Float)
    nr_ideal_function = Column(Float)

    def __init__(self, x, y, delta_y, nr_ideal_function):
        self.x = x
        self.y = y
        self.delta_y = delta_y
        self.nr_ideal_function = nr_ideal_function

base.metadata.create_all(engine)