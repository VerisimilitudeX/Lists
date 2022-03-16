# Lists:
* A collection data type, like a tuple
* A single variable that holds multiple values
* Values are usually all the same type
* Surrounded by [ ] symbols
* Items are separated by commas
  # Index:
  * The position of an item in a list
  * Each index corresponds to one item in a list
  * The 1st position in a list is index 0 * 1st position is index 0, 2nd position is index 1, 3rd position is index 2, etc.
  * Last index is always list length - 1
  # How to get or change a value in a list:
  * Access a value using list_name[index]
  * list[0] is pronounced:
  * "Item 0 in list"
  * "Item at index 0 in list"
  * "Item at position 0 in list"
  * "List sub 0"
  * variable = list_name[index] gets an item from a list
  * list_name[index] = variable replaces a value in a list
  * Only use indexes that are in the list * Indexes >= the list length are not valid * Indexes < 0 are not valid
  # How to get the length of a list:
  * Length is the number of items in a list
  * len(list_name) gives the length of a list
  * Returns an integer
  * Used to see what indexes are valid
  # How to change the length of a list:
  * list_name.append(item) adds an item to the end of a list
  * list_name.remove(item) removes the first matching item from a list * If an item is not in a list, remove will cause an error
  * item in list returns a boolean that tells whether the item is in the list
  * Use item in list as condition before removing * Example:
  *if "blue" in color_list:
          *color_list.remove("blue")
