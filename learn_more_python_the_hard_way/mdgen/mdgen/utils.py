import os
import markdown

def troll_directories(start):
	results = []

	# troll for all the directories like in find
	# traverse the directories for all files
	for root, dirs, files in os.walk(start):
		# for each file, see if pattern in filename
		for fname in files:
			# put the full path into the results
			results.append(os.path.join(root, fname))

	return results

def discover_targets(source, target, files):
	results = []

	# for each file
	for source_file in files:
		# strip extension of source file
		base, ext = os.path.splitext(source_file)
		path = base[len(source)+1:]
		target_dir = os.path.dirname(os.path.join(target, path))

		if not os.path.exists(target_dir):
			os.makedirs(target_dir)

		# append .html to filename
		target_file = os.path.join(target, path + ".html")

		results.append((source_file, target_file))

	return results

def generate_html(source_file, target_file):
	# open the source file 
	contents = open(source_file).read()

	# convert to markdown
	html = markdown.markdown(contents)

	# open output with .html
	with open(target_file, 'w') as f:
		# write html to .html
		f.write(html)

def convert_md_directory(source, target):
	# get all the files in the source directory
	sources = troll_directories(source)
	targets = discover_targets(source, target, sources)

	print targets

	for source_file, target_file in targets:
		generate_html(source_file, target_file)