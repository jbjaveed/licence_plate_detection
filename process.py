import glob, os
training_dataset_dir = 'custom_dataset'
destination_folder = 'custom_cfg'
# Percentage of images to be used for the test set
percentage_test = 10;
# Create and/or truncate train.txt and test.txt
file_train = open(destination_folder+'/train.txt', 'w')  
file_test = open(destination_folder+'/test.txt', 'w')
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(training_dataset_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(training_dataset_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(training_dataset_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1