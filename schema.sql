/*Project Phase 2                         CS 166 Database Management Systems  
Project Group #29
Matthew Underwood                       Instructor: V.Tsotras
ID 861-04-4121                      Section 22
munde001@ucr.edu                    TA: Karishma Dash
Jordan Meyer                            Instructor: V.Tsotras
ID 861-01-5184                      Section 21
jmeye006@ucr.edu                    TA: Samarth
*/


DROP TABLE User;
DROP TABLE Message;
DROP TABLE EducationDetails;
DROP TABLE WorkExperience;
DROP TABLE Connection;

CREATE TABLE User
(userid CHAR(10) NOT NULL UNIQUE,
    name CHAR(50),
    password CHAR(10) NOT NULL,
    email CHAR(50) NOT NULL,
    dateofbirth DATE,
    PRIMARY KEY userid );

CREATE TABLE Message
(messageid INTEGER NOT NULL AUTO_INCREMENT,
    senderid CHAR(10) NOT NULL,
    receiverid CHAR(10) NOT NULL,
    contents TEXT NOT NULL,
    sendtime TIMESTAMP NOT NULL,
    deletestatus INTEGER,
    status CHAR(30) NOT NULL,
    PRIMARY KEY messageid,
    FOREIGN  KEY senderid REFERENCES User,
    FOREIGN  KEY receiverid REFERENCES User  );


CREATE TABLE EducationDetails
(userid CHAR(10) NOT NULL,
    institutionname CHAR(50) NOT NULL,
    major CHAR(50) NOT NULL,
    degree CHAR(50) NOT NULL,
    startdate DATE,
enddate DATE,
PRIMARY KEY (userid, major, degree),
FOREIGN  KEY userid REFERENCES User );

CREATE TABLE WorkExperience
(userid CHAR(10) NOT NULL,
    company CHAR(50) NOT NULL,
    role CHAR(50) NOT NULL,
    location CHAR(50),
    startdate DATE NOT NULL,
enddate DATE,
PRIMARY KEY (userid, company, role, startdate), 
FOREIGN  KEY userid REFERENCES User );

CREATE TABLE Connection
(userid CHAR(10) NOT NULL,
    connectionid CHAR(10) NOT NULL,
    status CHAR(30) NOT NULL,
    PRIMARY KEY (connectionid, userid),
    FOREIGN  KEY userid REFERENCES User,
    FOREIGN  KEY connectionid REFERENCES User.userid);

