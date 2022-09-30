# Imports
from script_helper import Helper
from alive_progress import alive_it
import csv

def main():
    print('[LTI CHECK] launching script')
    helper = Helper()
    helper.authenticate()
    courses = helper.get_courses_ultra()
    content_list =[]
    print('[LTI CHECK] looping through courses')
    for c in alive_it(courses):
        helper.authenticate()
        LTI_content = helper.get_LTI_content_ultra(c["id"])
        for L in LTI_content:
            data_to_append = {
                'course_id':c["id"],
                'external_id':c["externalId"],
                'course_name':c["name"],
                'LTI_title':L["title"],
                'LTI_created':L["created"],
                'LTI_modified':L["modified"],                 
                'LTI_available':L["availability"]["available"]
                }
            content_list.append(data_to_append)
    print('[LTI CHECK] Generating CSV report')
    with open('./lti_report.csv','w',newline='') as csvfile:
        fieldnames = ['course_id','external_id','course_name','LTI_title','LTI_created','LTI_modified','LTI_available']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for c in content_list:
            writer.writerow(c)

if __name__ == "__main__":
    main()
