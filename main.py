from pyscript import document, display

def checkList (e) :

    zeph_list = ["Erin Rioflorido", "Inno Pena", "Mandy Cajanding", "Chloe Adlawan", "Meyer Cruz", "Audrey Tan", "Aleynah Redillas"]

    firstnm= document.getElementById("firstnm").value
    name= zeph_list

    confirm_name = firstnm() in zeph_list

    message = (f'Sorry{name}, you are not part of ZEPHYR.' , f'Yey! {name}, you are part of ZEPHYR.')

    document.getElementById("output1").innerHTML = message[confirm_name]