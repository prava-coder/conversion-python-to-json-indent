#Write a Python program to convert Python dictionary object (sort by key) to JSON data.
# Print the object members with indent level 4

import json
py_dict={
    "abc":"alphabets",
    "fname":"pravalli",
    "lname":"nalamothu",
    "age":20,
    "city":"ongole"

}

xy=json.dumps(py_dict,sort_keys=True,indent=4)
print(xy)