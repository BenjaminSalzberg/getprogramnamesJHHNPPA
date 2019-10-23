def main():
	# Columns = ["Name", "State", "Phone Number", "Link", "Care Type"]
	links = []
	names = []
	states = []
	phone_numbers = []
	care_type = []
	MAIN_LIST = []
	fo = open("file.html", "r")
	line = fo.read(10000000)
	fo.close()
	while line.__contains__("h3"):
		state_start = line.index("<h3")
		end_state = line.index("/h3")
		temp_state = line[state_start:end_state-1]
		begin_state = temp_state.index("</a> ")
		current_state = temp_state[begin_state+5:]
		# print(line)

		if line.__contains__("/div") and line.__contains__("div"):
			# print(current_state)
			division_start = line.index("div")
			division_end = line.index("/div")
			division = line[division_start:division_end]
			line = line[division_end+1:]
		else:
			print("Hi")
			break
		# break
		while division.__contains__("</p>") and division.__contains__("<p>"):
			para_start = division.index("<p>")
			state_div = division[para_start:]
			para_end = state_div.index("</p>")
			para = state_div[:para_end]
			next_para = division.index("</p>")
			division = division[next_para+4:]
			if para.__contains__("Adult Care"):
				if para.__contains__("("):
					phone_number_index = para.index("(")
					phone_number_prelim = para[phone_number_index:]
					if phone_number_prelim.__contains__("<br>"):
						phone_number_end = phone_number_prelim.index("<br>")
						phone_number = phone_number_prelim[:phone_number_end]
						phone_numbers.append(phone_number)
					else:
						phone_number = phone_number_prelim
						phone_numbers.append(phone_number_prelim)
				else:
					phone_number = "NO_PHONE_NUMBER"
					phone_numbers.append("NO_PHONE_NUMBER")
				name_index_end = para.index("</strong>")
				name = para[11:name_index_end]
				if para.__contains__("<a href="):
					link_index = para.index("<a href=")
					link_index_end = para.index(" class")
					link = para[link_index+9:link_index_end-1]
					links.append(link)
				else:
					link = "NO_LINK"
					links.append("NO_LINK")
				names.append(name)
				states.append(current_state)
				care_type.append("Adult Care")
				SUB_LIST = [name, current_state, phone_number, link, "Adult Care"]
				MAIN_LIST.append(SUB_LIST)
			elif para.__contains__("Pediatric Care"):
				pass
			elif para.__contains__("There are no resources at this time."):
				pass
			else:
				if para.__contains__("</strong>"):
					name_index_end = para.index("</strong>")
					name = para[11:name_index_end]
					names.append(name)
				else:
					name = "NO_NAME"
					names.append("NO_NAME")
				if para.__contains__("("):
					phone_number_index = para.index("(")
					phone_number_prelim = para[phone_number_index:]
					if phone_number_prelim.__contains__("<br>"):
						phone_number_end = phone_number_prelim.index("<br>")
						phone_number = phone_number_prelim[:phone_number_end]
						phone_numbers.append(phone_number)
					else:
						phone_number = phone_number_prelim
						phone_numbers.append(phone_number_prelim)
				else:
					phone_number = "NO_PHONE_NUMBER"
					phone_numbers.append("NO_PHONE_NUMBER")
				if para.__contains__("<a href=") and para.__contains__(" class"):
					link_index = para.index("<a href=")
					link_index_end = para.index(" class")
					link = para[link_index+9:link_index_end-1]
					links.append(link)
				else:
					link = "NO_LINK"
					links.append("NO_LINK")
				states.append(current_state)
				care_type.append("Unknown Care")
				SUB_LIST = [name, current_state, phone_number, link, "Unknown Care"]
				MAIN_LIST.append(SUB_LIST)
	print(len(MAIN_LIST))
	# write to csv
	file = open("demo.csv", "w")
	file.write("Name, State, Phone Number, Link, Care Type\n")
	for lst in MAIN_LIST:
		string = ""
		counter = 0
		for ele in lst:
			if counter != 0:
				string += ","
			if ele.__contains__(","):
				ele = ele.replace(",", "_")
			if ele.__contains__("<br>"):
				ele = ele.replace("<br>", " ")
			if ele.__contains__("\n"):
				ele = ele.replace("\n", " ")
			# &nbsp;
			if ele.__contains__("&nbsp;"):
				ele = ele.replace("&nbsp;", " ")
			# &ndash;
			if ele.__contains__("&ndash;"):
				ele = ele.replace("&ndash;", "-")
			# &rsquo;
			if ele.__contains__("&rsquo;"):
				ele = ele.replace("&rsquo;", "'")
			string += ele
			counter += 1
		string += "\n"
		file.write(string)
	file.close()


if __name__ == "__main__":
	main()
