import os
from tkinter import (Button, Frame, Label, LabelFrame, StringVar, Tk, messagebox, ttk)
from tkinter.constants import (BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y)

import cv2
import mysql.connector
from PIL import Image, ImageTk


class Student:
    def __init__(self, win_tk_root):  # constructor
        # setup for the mainframe of the window

        # variable declaration
        self.var_course = StringVar()
        self.var_department = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_name = StringVar()
        self.var_roll_no = StringVar()
        self.var_teacher_name = StringVar()
        self.var_photo_sample = StringVar()

        # window title
        self.root = win_tk_root
        self.root.title("Attendance System")

        # get screen dimensions
        screen_width = win_tk_root.winfo_screenwidth()
        screen_height = win_tk_root.winfo_screenheight()

        self.root.geometry("%dx%d+0+0" % (screen_width, screen_height))  # full screen window
        self.root.resizable(False, False)  # resizable window

        # setup content of the window

        # body background image

        bg_body_image = Image.open("project_images/img_bg_body.jpg")
        bg_body_image = bg_body_image.resize((screen_width,screen_height), Image.ANTIALIAS)
        self.bg_body_photo_image = ImageTk.PhotoImage(bg_body_image)
        bg_body_image_label = Label(self.root, image = self.bg_body_photo_image)
        bg_body_image_label.place(x = 0, y = 0, width = int(screen_width), height = int(screen_height))

        # title below header

        title_label = Label(bg_body_image_label, text = "Attendance Management System",
                            font = ("Times New Roman", 35, "bold"), background = "black", foreground = "cyan")
        title_label.place(x = 0, y = 0, width = int(screen_width), height = 65)

        # main frame

        main_frame = Frame(bg_body_image_label, border = 1, background = "white")
        main_frame.place(x = 0, y = 60, width = int(
            screen_width), height = int(screen_height))

        # left frame
        left_frame = LabelFrame(main_frame, border = 2, relief = RIDGE, text = "Student Details",
                                font = ("Times New Roman", 14, "bold"), background = "white")
        left_frame.place(x = 12, y = 12, width = 760, height = 740)

        # image
        left_frame_image = Image.open("project_images/img_students.jpg")
        left_frame_image = left_frame_image.resize((750, 130), Image.ANTIALIAS)
        self.left_frame_photo_image = ImageTk.PhotoImage(left_frame_image)
        left_frame_image_label = Label(left_frame, image = self.left_frame_photo_image, background = "white")
        left_frame_image_label.place(x = 5, y = 0, width = 750, height = 150)

        # course information frame

        course_info_frame = LabelFrame(left_frame, border = 3, relief = RIDGE, text = "Course Information",
                                       font = ("Times New Roman", 35, "bold"),
                                       background = "white")
        course_info_frame.place(x = 5, y = 155, width = 750, height = 150)
        # initializing and placing the field labels and combobox

        # course
        course_label = Label(course_info_frame, text = "Course", font = ("Times New Roman", 14, "bold"),
                             background = "white")
        course_label.grid(row = 0, column = 0, padx = 10, pady = 5)
        course_cb = ttk.Combobox(course_info_frame, textvariable = self.var_course,
                                 font = ("Times New Roman", 12, "bold"),
                                 background = "white")
        course_cb["values"] = ("Select", "B.Tech", "BCA", "B.Sc.(Hons.)")
        course_cb.current(0)
        course_cb.grid(row = 0, column = 1, padx = 2, pady = 12, sticky = W)

        # department
        department_label = Label(course_info_frame, text = "Department", font = ("Times New Roman", 14, "bold"),
                                 background = "white")
        department_label.grid(row = 0, column = 2, padx = 10, pady = 5)
        department_cb = ttk.Combobox(course_info_frame, textvariable = self.var_department,
                                     font = ("Times New Roman", 12, "bold"), background = "white")
        department_cb["values"] = (
            "Select", "Computer Sciences", "Information Technology", "Automation", "Cyber Security")
        department_cb.current(0)
        department_cb.grid(row = 0, column = 3, padx = 2, pady = 12, sticky = W)

        # year
        year_label = Label(course_info_frame, text = "Year", font = ("Times New Roman", 14, "bold"),
                           background = "white")
        year_label.grid(row = 1, column = 0, padx = 10, pady = 5)
        year_cb = ttk.Combobox(course_info_frame, textvariable = self.var_year, font = ("Times New Roman", 12, "bold"),
                               background = "white")
        year_cb["values"] = ("Select", "2020-21", "2021-22", "2022-23", "2023-24")
        year_cb.current(0)
        year_cb.grid(row = 1, column = 1, padx = 2, pady = 12, sticky = W)

        # semester
        semester_label = Label(course_info_frame, text = "Semester", font = ("Times New Roman", 14, "bold"),
                               background = "white")
        semester_label.grid(row = 1, column = 2, padx = 10, pady = 5)
        semester_cb = ttk.Combobox(course_info_frame, textvariable = self.var_semester,
                                   font = ("Times New Roman", 12, "bold"))
        semester_cb["values"] = ("Select", "2nd sem", "4th sem", "6th sem", "8th sem")
        semester_cb.current(0)
        semester_cb.grid(row = 1, column = 3, padx = 2, pady = 12, sticky = W)

        # student information frame
        student_info_frame = LabelFrame(left_frame, bd = 2, relief = RIDGE, text = "Student Information",
                                        font = ("Times New Roman", 14, "bold"), background = "white")
        student_info_frame.place(x = 5, y = 312, width = 750, height = 400)
        # initializing and placing field labels and entry

        # student name
        student_name_label = Label(student_info_frame, text = "Student Name : ", font = ("Times New Roman", 14, "bold"),
                                   background = "white")
        student_name_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
        student_name_entry = ttk.Entry(student_info_frame, textvariable = self.var_student_name, width = 20,
                                       font = ("Times New Roman", 12, "bold"), background = "white")
        student_name_entry.grid(row = 0, column = 1, padx = 10, sticky = W)

        # student roll_no
        student_roll_no_label = Label(student_info_frame, text = "Roll No. : ", font = ("Times New Roman", 14, "bold"),
                                      background = "white")
        student_roll_no_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
        student_roll_no_entry = ttk.Entry(student_info_frame, textvariable = self.var_roll_no,
                                          font = ("Times New Roman", 12, "bold"), background = "white")
        student_roll_no_entry.grid(row = 1, column = 1, padx = 10, sticky = W)

        # Teacher in charge details
        teacher_name_label = Label(student_info_frame, text = "T.I.C. : ", font = ("Times New Roman", 14, "bold"),
                                   background = "white")
        teacher_name_label.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)
        teacher_name_entry = ttk.Entry(student_info_frame, textvariable = self.var_teacher_name,
                                       font = ("Times New Roman", 12, "bold"), background = "white")
        teacher_name_entry.grid(row = 0, column = 3, padx = 10, sticky = W)

        # photo sample radio button
        photo_sample_rb = ttk.Radiobutton(student_info_frame, text = "Photo Sample", variable = self.var_photo_sample,
                                          value = "Yes")
        photo_sample_rb.grid(row = 1, column = 3, padx = 10, sticky = W)

        # buttons frame
        button_frame = Frame(student_info_frame, bd = 2, relief = RIDGE, background = "white")
        button_frame.place(x = 25, y = 200, width = 700, height = 70)

        # buttons

        save_button = Button(button_frame, text = "Save", command = self.save_data, width = 25,
                             font = ("Times New Roman", 12, "bold"), background = "teal", foreground = "white")
        save_button.grid(row = 0, column = 0)

        update_button = Button(button_frame, text = "Update", font = ("Times New Roman", 12, "bold"), width = 25,
                               background = "teal", foreground = "white", command = self.update_data)
        update_button.grid(row = 0, column = 1)

        delete_button = Button(button_frame, text = "Delete", font = ("Times New Roman", 12, "bold"), width = 25,
                               background = "teal", foreground = "white", command = self.delete_data)
        delete_button.grid(row = 0, column = 2)

        reset_button = Button(button_frame, text = "Reset", font = ("Times New Roman", 12, "bold"), width = 25,
                              background = "teal", foreground = "white", command = self.reset_fields)
        reset_button.grid(row = 1, column = 0)

        photo_sample_button = Button(button_frame, text = "Take Photo Sample", font = ("Times New Roman", 12, "bold"),
                                     width = 25, background = "teal", foreground = "white",
                                     command = self.take_photo_sample)
        photo_sample_button.grid(row = 1, column = 1)

        # right frame
        right_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = "Student Details",
                                 font = ("times new roman", 14, "bold"), background = "white")
        right_frame.place(x = 800, y = 12, width = 660, height = 580)

        # search system
        search_frame = LabelFrame(right_frame, bd = 2, relief = RIDGE, text = "Search System",
                                  font = ("times new roman", 14, "bold"), background = "white")
        search_frame.place(x = 5, y = 50, width = 650, height = 80)

        search_label = Label(search_frame, text = "Search By:", font = ("times new roman", 14, "bold"), bg = "white")
        search_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

        search_combo = ttk.Combobox(search_frame, font = ("times new roman", 12, "bold"), state = "read only")
        search_combo["values"] = ("Select", "Roll_no")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx = 2, pady = 12, sticky = W)

        search_entry = ttk.Entry(search_frame, width = 12, font = ("times new roman", 12, "bold"))
        search_entry.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)

        search_button = Button(search_frame, text = "Search", width = 10, font = ("times new roman", 12, "bold"),
                               bg = "teal",
                               fg = "white")
        search_button.grid(row = 0, column = 3, padx = 4)

        show_all_button = Button(search_frame, text = "Show All", width = 10, font = ("times new roman", 12, "bold"),
                                 bg = "teal", fg = "white")
        show_all_button.grid(row = 0, column = 4, padx = 4)

        # table frame
        table_frame = Frame(right_frame, bd = 2, relief = RIDGE)
        table_frame.place(x = 5, y = 212, width = 650, height = 350)

        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns = (
            "department", "course", "year", "semester", "student_name", "roll_no", "teacher_name", "photo_sample"),
                                          xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)

        self.student_table.heading("department", text = "Department")
        self.student_table.heading("course", text = "Course")
        self.student_table.heading("year", text = "Year")
        self.student_table.heading("semester", text = "Semester")
        self.student_table.heading("student_name", text = "Student Name")
        self.student_table.heading("roll_no", text = "Roll No")
        self.student_table.heading("teacher_name", text = "Teacher Name")
        self.student_table.heading("photo_sample", text = "Photo Sample")

        self.student_table["show"] = "headings"
        self.student_table.column("department", width = 120)
        self.student_table.column("course", width = 120)
        self.student_table.column("year", width = 120)
        self.student_table.column("semester", width = 120)
        self.student_table.column("student_name", width = 120)
        self.student_table.column("roll_no", width = 120)
        self.student_table.column("teacher_name", width = 120)
        self.student_table.column("photo_sample", width = 120)
        self.student_table.pack(fill = BOTH, expand = 1)

        self.student_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()
        # design section ends here

    # function definitions

    # fetch_data function definition
    def fetch_data(self):
        cob = mysql.connector.connect(host = "localhost", username = "root", password = "toor",
                                      database = "attendance_system_using_face_recognition")
        my_cursor = cob.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for iterator in data:
                self.student_table.insert("", END, values = iterator)
            cob.commit()
        cob.close()

    # get_cursor function definition
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_student_name.set(data[4]),

        self.var_roll_no.set(data[5]),

        self.var_teacher_name.set(data[6]),
        self.var_photo_sample.set(data[7])

    # save_data function definition
    def save_data(self):
        if self.var_department.get() == "Select Department" or self.var_student_name.get() == "" or self.var_roll_no.get() == "":
            messagebox.showerror("Error Add Data", "All Fields are required", parent = self.root)
        else:
            try:
                cob = mysql.connector.connect(
                    host = "localhost", username = "root", password = "toor",
                    database = "attendance_system_using_face_recognition")
                my_cursor = cob.cursor()
                if self.var_photo_sample.get() == "":
                    var_ps = "No"
                else:
                    var_ps = self.var_photo_sample.get()
                my_cursor.execute("Insert into student values(%s, %s, %s, %s, %s, %s, %s, %s)   ",
                                  (self.var_department.get(), self.var_course.get(
                                  ), self.var_year.get(), self.var_semester.get(), self.var_student_name.get(),
                                   self.var_roll_no.get(), self.var_teacher_name.get(), var_ps))
                cob.commit()
                self.fetch_data()
                cob.close()
                messagebox.showinfo("Success Save Data", "Student details have been successfully added to the database",
                                    parent = self.root)
            except Exception as e:
                messagebox.showerror("Error Save data", f"Due to : {str(e)}", parent = self.root)

    # update_data function definition

    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_student_name.get() == "" or self.var_roll_no.get() == "":
            messagebox.showerror("Error update data", "All fields are required", parent = self.root)
        else:
            try:
                var_update = messagebox.askyesno("Update data", "Do you want to update Student details ?",
                                                 parent = self.root)
                if var_update > 0:
                    cob = mysql.connector.connect(host = "localhost", username = "root", password = "toor",
                                                  database = "attendance_system_using_face_recognition")
                    my_cursor = cob.cursor()
                    if self.var_photo_sample.get() == "":
                        var_ps = "No"
                    else:
                        var_ps = self.var_photo_sample.get()
                    my_cursor.execute(
                        "update student set department = %s, course = %s, year = %s, semester = %s, student_name = %s, teacher_name = %s, photo_sample = %s where roll_no = %s",
                        (self.var_department.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                         self.var_student_name.get(), self.var_teacher_name.get(), var_ps, self.var_roll_no.get()))
                    if my_cursor.rowcount == 1:
                        messagebox.showinfo("Success Update Data",
                                            "Student details successfully updated in the database !",
                                            parent = self.root)
                    cob.commit()
                    cob.close()
                elif var_update == 0:
                    messagebox.showinfo("Error Update Data", "Permission denied by user !", parent = self.root)
                self.fetch_data()
            except Exception as e:
                messagebox.showerror("Error Update Data", f"Due to: {str(e)}", parent = self.root)

    # delete_data function definition
    def delete_data(self):
        if self.var_roll_no.get() == "":
            messagebox.showerror("Error delete data", "Student roll_no required !", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Data", "Do you want to delete this student' details ?",
                                             parent = self.root)
                if delete > 0:
                    cob = mysql.connector.connect(host = "localhost", username = "root", password = "toor",
                                                  database = "attendance_system_using_face_recognition")
                    my_cursor = cob.cursor()
                    my_cursor.execute("delete from student where roll_no = %s", (self.var_roll_no.get(),))
                    cob.commit()
                    cob.close()
                else:
                    if not delete:
                        return
                self.fetch_data()
                self.reset_fields()
                messagebox.showinfo("Delete Data", "Successfully deleted student details !", parent = self.root)
            except Exception as e:
                messagebox.showerror("Error Delete Data", f"Due to:{str(e)}", parent = self.root)

    # reset fields function definition
    def reset_fields(self):
        self.var_department.set("Select")
        self.var_course.set("Select")
        self.var_year.set("Select")
        self.var_semester.set("Select")
        self.var_student_name.set("")
        self.var_roll_no.set("")
        self.var_teacher_name.set("")
        self.var_photo_sample.set("")

    # take photo sample function definition
    def take_photo_sample(self):
        if self.var_department.get() == "Select" or self.var_roll_no.get() == "" or self.var_student_name.get() == "":
            messagebox.showerror("Error Take Photo Sample", "All fields are required ! ", parent = self.root)
        else:  # updating any change in student details and checking if student has been registered or not too
            try:
                # load predefined data on face frontal from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img_user):
                    gray = cv2.cvtColor(img_user, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.1, 10)
                    # scaling factor = 1.1
                    # minimum neighbour = 10

                    for (x, y, w, h) in faces:
                        face_cropped = img_user[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "face_data/user_" + str(self.var_roll_no.get()) + "_" + str(img_id) + ".jpg"
                        cv2.imwrite(os.path.join(file_name_path), face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result Take Photo Sample", "Dataset Generation complete !")
            except Exception as e:
                messagebox.showerror("Error Delete Data", f"Due to:{str(e)}", parent = self.root)


# def on_focus_out(event):
#     if event.widget == root:
#         root.destroy()
#         print(" student window closed")


if __name__ == '__main__':
    winTk = Tk()
    flag = True
    obj = Student(winTk)


    def on_closing():
        close = messagebox.askyesno("Close", "Are you sure you want to exit the System ?")
        if close:
            winTk.destroy()


    if flag:
        winTk.protocol("WM_DELETE_WINDOW", on_closing)
    winTk.mainloop()

    # not working when child tk windows open from inside of parent tk window
    # def on_closing():
    #     close = messagebox.askyesno("Close", "Are you sure you want to exit the System ?")
    #     if close:
    #         root.destroy()
    # if flag:
    #   root.protocol("WM_DELETE_WINDOW", on_closing)
    # root.protocol("Student Details Window",root.iconify)
    # root.bind("<FocusOut>", on_focus_out)
