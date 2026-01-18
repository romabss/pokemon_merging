import time


class Pokemon:
    def __init__(self, name, p_type, hp, gen, stage):
        self.name = name
        self.p_type = p_type
        self.hp = hp
        self.gen = gen
        self.stage = stage


    def __repr__(self):
        return f"{self.name:18} | Type: {self.p_type:10} | HP: {self.hp:3} | Gen: {self.gen} | Stage: {self.stage}"




# pokemon type order
TYPE_ORDER = {
    "Normal": 0, "Fire": 1, "Water": 2, "Electric": 3, "Grass": 4,
    "Ice": 5, "Fighting": 6, "Poison": 7, "Ground": 8, "Flying": 9,
    "Psychic": 10, "Bug": 11, "Rock": 12, "Ghost": 13, "Dragon": 14,
    "Dark": 15, "Steel": 16, "Fairy": 17
}




# pokemon na 18 piraso
pokedex = [
    Pokemon("Greninja", "Water", 72, 6, 2),
    Pokemon("Bulbasaur", "Grass", 45, 1, 0),
    Pokemon("Lucario", "Fighting", 70, 4, 1),
    Pokemon("Pikachu", "Electric", 35, 1, 0),
    Pokemon("Gardevoir", "Psychic", 68, 3, 2),
    Pokemon("Charmander", "Fire", 39, 1, 0),
    Pokemon("Froakie", "Water", 41, 6, 0),
    Pokemon("Ivysaur", "Grass", 60, 1, 1),
    Pokemon("Zoroark", "Dark", 60, 5, 1),
    Pokemon("Charizard", "Fire", 78, 1, 2),
    Pokemon("Riolu", "Fighting", 40, 4, 0),
    Pokemon("Empoleon", "Water", 84, 4, 2),
    Pokemon("Frogadier", "Water", 54, 6, 1),
    Pokemon("Blaziken", "Fire", 80, 3, 2),
    Pokemon("Eevee", "Normal", 55, 1, 0),
    Pokemon("Sylveon", "Fairy", 95, 6, 1),
    Pokemon("Dark Tyranitar", "Rock", 100, 2, 2),
    Pokemon("Abra", "Psychic", 25, 1, 0)
]




# for backups to kase may function na pwede makita yung unsorted list at ito yung iaaccess natin
CPY_POKEDEX = list(pokedex)




#  tuple values siya para don sa proper na pagkakasunod-sunod para sa final output
def get_multi_sort_key(p):
    return (p.stage, p.gen, p.hp, TYPE_ORDER.get(p.p_type, 99), p.name)




def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)


    return merge(left, right, key)




def merge(left, right, key):
    result = []
    i = j = 0


   
    while i < len(left) and j < len(right):


        if key == 'overall':
            val_left = get_multi_sort_key(left[i])
            val_right = get_multi_sort_key(right[j])
        elif key == 'p_type':
            val_left = TYPE_ORDER.get(left[i].p_type, 99)
            val_right = TYPE_ORDER.get(right[j].p_type, 99)
        else:
            val_left = getattr(left[i], key)
            val_right = getattr(right[j], key)


        if val_left <= val_right:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result.extend(left[i:])
    result.extend(right[j:])
    return result




def print_pokedex(data_list):
    print(f"\n{'Name':18} | {'Type':16} | {'HP':7} | {'Gen':6} | {'Stage'}")
    print("-" * 67)
    for p in data_list:
        print(p)




def menu():
    global pokedex


    while True:
        print("\n--- POKEMON DATABASE ---")
        print("a. Evolution Stage")
        print("b. Generation")
        print("c. By HP")
        print("d. Pokemon Type")
        print("e. Alphabetical Name")
        print("f. Final Sort")
        print("g. Unsorted List")
        print("h. Exit")


        choice = input("\nSelect an option: ").lower()


        key_map = {
            'a': 'stage',
            'b': 'gen',
            'c': 'hp',
            'd': 'p_type',
            'e': 'name',
            'f': 'overall'
        }


        if choice == 'h':
            print("Successfully Exited The Program!")
            break


        elif choice == 'g':
            print("\n--- Unsorted List ---")
            print_pokedex(CPY_POKEDEX)


        elif choice in key_map:
            start = time.perf_counter()      # timer start
            pokedex = merge_sort(pokedex, key_map[choice])
            end = time.perf_counter()        # timer end


            elapsed = end - start


            print(f"\n--- SORTED BY {key_map[choice].upper()} ---")
            print_pokedex(pokedex)


            print(f"\nSorting Time: {elapsed:.8f} seconds")
            print(f"Sorting Time: {elapsed * 1_000_000:.2f} microseconds")


        else:
            print("Invalid selection. Try again.")




if __name__ == "__main__":
    menu()

