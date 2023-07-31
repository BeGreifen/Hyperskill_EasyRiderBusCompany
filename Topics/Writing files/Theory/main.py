#  You can experiment here, it won’t be checked
# read animals.txt
# and write animals_new.txt
ori_file = open("animals.txt","r")
ori_lines = ori_file.readlines()
ori_file.close()

ori_lines = [line.rstrip() for line in ori_lines]
out_line = " ".join(ori_lines) + "\n"

out_file = open("animals_new.txt","w")
out_file.write(out_line)
out_file.close()

