def string_rotation(str_ori, str_rot):
    str_rot_double = str_rot + str_rot
    if str_rot_double.find(str_ori) > 0:
        return True
    return False

#This is O(N) time.
#Concatenating two rotated strings takes 2N time
#Checking for the substring takes less than O(N) time, so it is absorbed

print(string_rotation("apple", "pleap"))