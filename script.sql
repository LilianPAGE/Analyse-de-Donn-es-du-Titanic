#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Navire
#------------------------------------------------------------

CREATE TABLE Navire(
        ID_Navire       Int  Auto_increment  NOT NULL ,
        Nom_Navire      Varchar (50) NOT NULL ,
        Date_Couler     Date ,
        Raison_Naufrage Varchar (50)
	,CONSTRAINT Navire_PK PRIMARY KEY (ID_Navire)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Personne
#------------------------------------------------------------

CREATE TABLE Personne(
        PassengerId Int  Auto_increment  NOT NULL ,
        Survived    Int,
        Pclass      Int,
        Name        Varchar (50) ,
        Sex         Varchar (50) ,
        Age         Float ,
        SibSp       Int ,
        Parch       Int ,
        Ticket      Varchar (50) ,
        Fare        Float ,
        Cabin       Varchar (50) ,
        Embarked    Varchar (50) ,
        ID_Navire   Int
	,CONSTRAINT Personne_PK PRIMARY KEY (Id_Passager)

	,CONSTRAINT Personne_Navire_FK FOREIGN KEY (ID_Navire) REFERENCES Navire(ID_Navire)
)ENGINE=InnoDB;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\train.csv'
INTO TABLE Personne
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
SET ID_Navire = "Titanic";
