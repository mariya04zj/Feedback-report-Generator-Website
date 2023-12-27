from patient import views


def myfunction(temp_file):
    import numpy as numpy,pandas as pd, matplotlib.pyplot as plt, seaborn as sns
    import dataframe_image as dfi

    patient_data=pd.read_csv(temp_file.name,skip_blank_lines=True)
    pd.set_option("display.max_columns" and "display.max_rows",None)

    new_column_names = ['Date','Name','Patient ID','City Of Residence','Phone number','Age','Gender','Department','Help Desk Services' ,'Hospital Processes','Waiting Time for OPD','Waiting time for admission and discharge procedures','Availability of Doctors',
                    'Punctuality of doctors','Quality of doctors','Availability of specialists','Accuracy of diagnosis','Quality of infrastructure',
                    'Quality and Availability of medical equipment','General staff behaviour','Nursing staff response time','Overall efficiency of nursing staff','Quality of Diagnostic Services','Availability of drugs','Digital Health and HMIS','Pre and post operation/treatment care and guidance',
                    'Emergency Handling','Efficiency of EMR system','Use of telemedicine','Hygiene and cleanliness in the facility','Quality and Quantity of food provided',
                    'Amenities for family and relatives','Overall experience in the healthcare facility','Possibility of you visiting again']

    if len(new_column_names) != len(patient_data.columns):
     raise ValueError("The number of new column names should match the number of columns in the CSV file.")


    patient_data.columns = new_column_names
    patient_data=patient_data.drop(['Name','Phone number','Patient ID'],axis=1,inplace=False)




    #PIE CHARTS
    column_name="Gender"
    category_counts=patient_data[column_name].value_counts()
    plt.figure(figsize=(8, 8))  # Optional: Set the figure size
    plot1=plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"Pie Chart for {column_name}")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # Save the plot before displaying it
    plt.savefig('/Users/mariyajeeranwala/Desktop/JANGO/patient/static/gender_piechart.png')

    column_name="Department"
    category_counts=patient_data[column_name].value_counts()
    plt.figure(figsize=(8, 8))  # Optional: Set the figure size
    plot2=plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"Pie Chart for {column_name}")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # Save the plot before displaying it
    plt.savefig('/Users/mariyajeeranwala/Desktop/JANGO/patient/static/dept_piechart.png')

    column_name="City Of Residence"
    category_counts=patient_data[column_name].value_counts()
    plt.figure(figsize=(8, 8))  # Optional: Set the figure size
    plot3=plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"Pie Chart for {column_name}")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # Save the plot before displaying it
    plt.savefig('/Users/mariyajeeranwala/Desktop/JANGO/patient/static/city_piechart.png')

    age_bins = [0, 18, 30, 40, 50, 60, 100]
    age_labels = ["0-18", "19-30", "31-40", "41-50", "51-60", "61+"]

    # Create age group categories
    patient_data['AgeGroup'] = pd.cut(patient_data['Age'], bins=age_bins, labels=age_labels)

    # Count the occurrences of each age group
    age_group_counts = patient_data['AgeGroup'].value_counts()

    plt.figure(figsize=(8, 8)) 
    plt.pie(age_group_counts, labels=age_group_counts.index, autopct='%1.1f%%', startangle=140)

    # Optional: Customize the plot
    plt.title("Pie Chart for Age Groups")
    plt.axis('equal')

    # Show the plot
    plt.savefig('/Users/mariyajeeranwala/Desktop/JANGO/patient/static/age_piechart.png')


    import pandas as pd
    #DESCRIPTIVE STATS
    Statistical_Data=pd.DataFrame(patient_data.describe())
    dfs1=Statistical_Data.iloc[:, 0:6]
    dfs2=Statistical_Data.iloc[:, 6:12]
    dfs3=Statistical_Data.iloc[:, 12:18]
    dfs4=Statistical_Data.iloc[:, 18:26]
    dfi.export(dfs1, '/Users/mariyajeeranwala/Desktop/JANGO/patient/static/Part1.png')
    dfi.export(dfs2, '/Users/mariyajeeranwala/Desktop/JANGO/patient/static/Part2.png')
    dfi.export(dfs3, '/Users/mariyajeeranwala/Desktop/JANGO/patient/static/Part3.png')
    dfi.export(dfs4, '/Users/mariyajeeranwala/Desktop/JANGO/patient/static/Part4.png')

    #DEPARTMENT WISE ANALYSIS
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Assuming 'patient_data' is your DataFrame

    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 12))

    # Boxplot for 'Availability of specialists'
    box_plot1 = sns.boxplot(x="Department", y="Availability of specialists", data=patient_data, ax=axes[0])

    ax = box_plot1.axes
    lines = ax.get_lines()
    categories = ax.get_xticks()

    for cat in categories:
        y = round(lines[4+cat*6].get_ydata()[0], 1)
        ax.text(
        cat, 
        y, 
        f'{y}', 
        ha='center', 
        va='center', 
        fontweight='bold', 
        size=10,
        color='white',
        bbox=dict(facecolor='#445A64'))

    box_plot1.figure.tight_layout()
    box_plot1.set_xticklabels(box_plot1.get_xticklabels(), rotation=90)


    # Boxplot for 'Accuracy of diagnosis'
    box_plot2 = sns.boxplot(x="Department", y="Accuracy of diagnosis", data=patient_data, ax=axes[1])

    ax = box_plot2.axes
    lines = ax.get_lines()
    categories = ax.get_xticks()

    for cat in categories:
        y = round(lines[4+cat*6].get_ydata()[0], 1)
        ax.text(
        cat, 
        y, 
        f'{y}', 
        ha='center', 
        va='center', 
        fontweight='bold', 
        size=10,
        color='white',
        bbox=dict(facecolor='#445A64'))

    box_plot2.figure.tight_layout()
    box_plot2.set_xticklabels(box_plot2.get_xticklabels(), rotation=90)

    # Boxplot for 'Quality of doctors'
    box_plot3 = sns.boxplot(x="Department", y="Quality of doctors", data=patient_data, ax=axes[2])

    ax = box_plot3.axes
    lines = ax.get_lines()
    categories = ax.get_xticks()

    for cat in categories:
        y = round(lines[4+cat*6].get_ydata()[0], 1)
        ax.text(
        cat, 
        y, 
        f'{y}', 
        ha='center', 
        va='center', 
        fontweight='bold', 
        size=10,
        color='white',
        bbox=dict(facecolor='#445A64'))

    box_plot3.figure.tight_layout()
    box_plot3.set_xticklabels(box_plot3.get_xticklabels(), rotation=90)

    bp3=box_plot3.get_figure()
    bp3.savefig('/Users/mariyajeeranwala/Desktop/JANGO/patient/static/dept_analysis.png')



    import seaborn as sns
    import matplotlib.pyplot as plt

    # Assuming 'patient_data' is your DataFrame

    # Calculate the Satisfaction_Score
    #SATISFACTION PLOTS:
    # Using map function

    patient_data_1 = patient_data.loc[: , patient_data.columns != "Digital Health and HMIS"]

    numeric_columns = patient_data.select_dtypes(include='number').columns
    numm=patient_data[numeric_columns].drop('Age', axis=1)
    patient_data_1['Satisfaction_Score']=numm.mean(axis=1)

    # Create subplots
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, 16))

    # Boxplot for 'Department'
    box_plot4 = sns.boxplot(x="Department", y="Satisfaction_Score", data=patient_data_1, ax=axes[0])

    ax = box_plot4.axes
    lines = ax.get_lines()
    categories = ax.get_xticks()

    for cat in categories:
        y = round(lines[4 + cat * 6].get_ydata()[0], 1)
        ax.text(
        cat,
        y,
        f'{y}',
        ha='center',
        va='center',
        fontweight='bold',
        size=10,
        color='white',
        bbox=dict(facecolor='#445A64'))

    box_plot4.figure.tight_layout()
    box_plot4.set_xticklabels(box_plot4.get_xticklabels(), rotation=90)

    # Boxplot for 'Gender'
    box_plot5 = sns.boxplot(x="Gender", y="Satisfaction_Score", data=patient_data_1, ax=axes[1])

    ax = box_plot5.axes
    lines = ax.get_lines()
    categories = ax.get_xticks()

    for cat in categories:
        y = round(lines[4 + cat * 6].get_ydata()[0], 1)
        ax.text(
        cat,
        y,
        f'{y}',
        ha='center',
        va='center',
        fontweight='bold',
        size=10,
        color='white',
        bbox=dict(facecolor='#445A64'))

    box_plot5.figure.tight_layout()

    # Boxplot for 'City Of Residence'
    box_plot6 = sns.boxplot(x="City Of Residence", y="Satisfaction_Score", data=patient_data_1, ax=axes[2])

    ax = box_plot6.axes
    lines = ax.get_lines()
    categories = ax.get_xticks()

    for cat in categories:
        y = round(lines[4 + cat * 6].get_ydata()[0], 1)
        ax.text(
        cat,
        y,
        f'{y}',
        ha='center',
        va='center',
        fontweight='bold',
        size=10,
        color='white',
        bbox=dict(facecolor='#445A64'))

    box_plot6.figure.tight_layout()
    box_plot6.set_xticklabels(box_plot6.get_xticklabels(), rotation=90)

    # Boxplot for 'Age Group'
    patient_data_1.loc[patient_data_1['Age']<18, 'age_group'] = '<18'
    patient_data_1.loc[patient_data_1['Age'].between(18,30), 'age_group'] = '18-30'
    patient_data_1.loc[patient_data_1['Age'].between(30,40), 'age_group'] = '30-40'
    patient_data_1.loc[patient_data_1['Age'].between(40,50), 'age_group'] = '40-50'
    patient_data_1.loc[patient_data_1['Age'].between(50,60), 'age_group'] = '50-60'
    patient_data_1.loc[patient_data_1['Age'].between(60,70), 'age_group'] = '60-70'
    patient_data_1.loc[patient_data_1['Age']>70, 'age_group'] = '>70'
    box_plot7 = sns.boxplot(x="age_group", y="Satisfaction_Score", data=patient_data_1, ax=axes[3])

    ax = box_plot7.axes
    lines = ax.get_lines()
    categories = ax.get_xticks()

    for cat in categories:
        y = round(lines[4 + cat * 6].get_ydata()[0], 1)
        ax.text(
            cat,
            y,
            f'{y}',
            ha='center',
            va='center',
            fontweight='bold',
            size=10,
            color='white',
            bbox=dict(facecolor='#445A64'))

    box_plot7.figure.tight_layout()
    box_plot7.set_xticklabels(box_plot7.get_xticklabels(), rotation=90)
    bp7=box_plot7.get_figure()
    bp7.savefig('/Users/mariyajeeranwala/Desktop/JANGO/patient/static/satis_scores.png')

    plt.show()

    #heatmap
    correlation_matrix = patient_data[numeric_columns].corr()
    plt.figure(figsize=(20, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.show()
    plt.savefig('/Users/mariyajeeranwala/Desktop/JANGO/patient/static/heatmap_total.png')


    #SCORES:

    #OVERALL HOSPITAL SCORE
    # Assuming 'Statistical_Data' is your DataFrame

    # Extract the relevant row of data
    Statistical_Data_1 = Statistical_Data.iloc[1, 2:]

    # Calculate the cumulative mean score
    cumulative_mean = Statistical_Data_1.mean()

    # Example usage:
    float_rating_overall = cumulative_mean

    # Ensure the rating is between 0 and 10
    float_rating_overall = max(0, min(10, float_rating_overall))

    # Calculate the number of filled stars
    filled_stars_overall = round(float_rating_overall)

    # Calculate the number of empty stars
    empty_stars_overall = 10 - filled_stars_overall

    # Create the visual representation
    visual_rating_overall = '★' * filled_stars_overall + '☆' * empty_stars_overall

    # Print the result for Overall Hospital Score
    print('Overall Hospital Score =', float_rating_overall, '->', visual_rating_overall)

    # Rating for Facilities
    facilities_scores = patient_data[['Quality of infrastructure', 'Quality and Quantity of food provided',
                                'Efficiency of EMR system', 'Hygiene and cleanliness in the facility',
                                'Quality and Availability of medical equipment', 'Use of telemedicine']].mean()
    facilities_average_score = facilities_scores.mean()

    # Example usage:
    float_rating_facilities = facilities_average_score

    # Ensure the rating is between 0 and 10
    float_rating_facilities = max(0, min(10, float_rating_facilities))

    # Calculate the number of filled stars
    filled_stars_facilities = round(float_rating_facilities)

    # Calculate the number of empty stars
    empty_stars_facilities = 10 - filled_stars_facilities

    # Create the visual representation
    visual_rating_facilities = '★' * filled_stars_facilities + '☆' * empty_stars_facilities

    # Print the result for Facilities
    print('Rating of Facilities =', float_rating_facilities, '->', visual_rating_facilities)

    # Rating for Staff
    staff_scores = patient_data[['Availability of Doctors', 'Punctuality of doctors', 'Quality of doctors',
                            'Accuracy of diagnosis', 'General staff behaviour', 'Nursing staff response time',
                            'Emergency Handling']].mean()
    staff_average_score = staff_scores.mean()

    # Example usage:
    float_rating_staff = staff_average_score

    # Ensure the rating is between 0 and 10
    float_rating_staff = max(0, min(10, float_rating_staff))

    # Calculate the number of filled stars
    filled_stars_staff = round(float_rating_staff)

    # Calculate the number of empty stars
    empty_stars_staff = 10 - filled_stars_staff

    # Create the visual representation
    visual_rating_staff = '★' * filled_stars_staff + '☆' * empty_stars_staff

    # Print the result for Staff
    print('Rating of Staff =', float_rating_staff, '->', visual_rating_staff)

    # Rating for Administration
    admin_scores = patient_data[['Help Desk Services', 'Waiting time for admission and discharge procedures',
                            'Waiting Time for OPD', 'Pre and post operation/treatment care and guidance']].mean()
    admin_average_score = admin_scores.mean()

    # Example usage:
    float_rating_admin = admin_average_score

    # Ensure the rating is between 0 and 10
    float_rating_admin = max(0, min(10, float_rating_admin))

    # Calculate the number of filled stars
    filled_stars_admin = round(float_rating_admin)

    # Calculate the number of empty stars
    empty_stars_admin = 10 - filled_stars_admin

    # Create the visual representation
    visual_rating_admin = '★' * filled_stars_admin + '☆' * empty_stars_admin

    # Print the result for Administration
    print('Rating of Administration =', float_rating_admin, '->', visual_rating_admin)

    # Your admin rating containing the '★' character
    star_character1 = visual_rating_admin

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Draw the '★' character at the center of the figure
    ax.text(0.5, 0.5, star_character1, fontsize=20, color="black",
    ha='center', va='center', transform=ax.transAxes)

    # Remove axis ticks and labels for a clean image
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Save the figure as a PNG file
    plt.savefig("/Users/mariyajeeranwala/Desktop/JANGO/patient/static/visual_rating_admin.png", format="png", bbox_inches="tight", pad_inches=0, dpi=300)
    plt.close()

    star_character2 = visual_rating_staff

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Draw the '★' character at the center of the figure
    ax.text(0.5, 0.5, star_character1, fontsize=20, color="black",
    ha='center', va='center', transform=ax.transAxes)

    # Remove axis ticks and labels for a clean image
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Save the figure as a PNG file
    plt.savefig("/Users/mariyajeeranwala/Desktop/JANGO/patient/static/visual_rating_staff.png", format="png", bbox_inches="tight", pad_inches=0, dpi=300)
    plt.close()

    star_character3 = visual_rating_facilities

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Draw the '★' character at the center of the figure
    ax.text(0.5, 0.5, star_character3, fontsize=20, color="black",
    ha='center', va='center', transform=ax.transAxes)

    # Remove axis ticks and labels for a clean image
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Save the figure as a PNG file
    plt.savefig("/Users/mariyajeeranwala/Desktop/JANGO/patient/static/visual_rating_facilities.png", format="png", bbox_inches="tight", pad_inches=0, dpi=300)
    plt.close()

    star_character4 = visual_rating_overall

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Draw the '★' character at the center of the figure
    ax.text(0.5, 0.5, star_character4, fontsize=20, color="black",
    ha='center', va='center', transform=ax.transAxes)

    # Remove axis ticks and labels for a clean image
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Save the figure as a PNG file
    plt.savefig("/Users/mariyajeeranwala/Desktop/JANGO/patient/static/visual_rating_overall.png", format="png", bbox_inches="tight", pad_inches=0, dpi=300)
    plt.close()
