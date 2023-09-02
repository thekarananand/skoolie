sample = {
    "thekarananand@gmail.com" : {
        "PASSWORD" : "1234$",
        "PREFERED NAME" : "Karan",
        "DATA" : {
            "NAME" : "Karan Anand",
            "ROLLNO" : "21109055",
            "EMAIL" : "thekarananand@gmail.com",
            "YEAR" : "3",
            "PROGRAM" : "BTECH",
            "BRANCH" : "ICE",
            "CONTACT" : "EMAIL",
        }
    },

    "nitish@gmail.com" : {
        "PASSWORD" : "6969",
        "PREFERED NAME" : "Nitish",
        "DATA" : {
            "NAME" : "Nitish Garg",
            "ROLLNO" : "21109074",
            "EMAIL" : "nitish@gmail.com",
            "YEAR" : "3",
            "PROGRAM" : "BTECH",
            "BRANCH" : "ICE",
            "CONTACT" : "EMAIL",
        }
    },
}

try :
    print (sample["hgib"]) 

except KeyError :
    print ("Wrong Key")