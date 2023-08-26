#Christopher Singleton
def main():
    male_students = int(input('Number of male students: '))
    female_students = int(input('Number of female students: '))
    
    combined_students = male_students + female_students
    
    m_perc = ("%.2f%%" % (100 * male_students/combined_students))
    f_perc = ("%.2f%%" % (100 * female_students/combined_students))
    
    print (f'The total number of students: \t \t {combined_students}')
    print (f'The number of males and females \t {male_students} \t \t {female_students}')
    print (f'The percentage of males and females \t {m_perc} \t {f_perc}')
    

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
