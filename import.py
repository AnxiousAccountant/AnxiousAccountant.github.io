import csv


import os, shutil
folder = '_posts/BeersPosts'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))



with open('_data/beer.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Creating Files: \n")
        else:
            f = open(f'_posts/BeersPosts/{row[1]}', "w")
            if row[47] == "Y":
                tags = 'beers, recent-beer'
            else:
                tags = 'beers'
            f.write(f'''--- 
title: {row[6]}
date: {row[26]}
last_modified_at: {row[48]}
firsttaste: {row[25]}
categories: [Non-Alcoholic Beers] 
tags: [{tags}] 
image: 
    src: {row[4]}
    height: 240 
    width: 240 
    alt: {row[5]}
--- 

{{% include beertable.md %}} 
            ''')

            f.close()
        line_count += 1
    print(f'Processed {line_count} lines.')
