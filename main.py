from student_details import Student
from train_face_data import TrainFaceData
from detect_face import DetectFace
from update_attendance import AttendanceManager
from tkinter import Button, Label, Tk, Toplevel, messagebox
from PIL import Image, ImageTk

parent_open = False
child_open = False


class AttendanceSystem:

    def __init__(self, win_tk_root):  # constructor

        # setup for the mainframe of the window

        # window title
        self.root = win_tk_root
        self.root.title("Attendance System")

        # get screen dimensions
        screen_width = win_tk_root.winfo_screenwidth()
        screen_height = win_tk_root.winfo_screenheight()

        self.root.geometry("%dx%d+0+0" % (screen_width, screen_height))  # full screen window
        self.root.resizable(False, False)  # resizable window

        # setup content of the window

        # header image top left

        header_tl_image = Image.open("project_images/img_university.jpg")
        header_tl_image = header_tl_image.resize((int(screen_width / 3), 130), Image.ANTIALIAS)
        self.header_tl_photo_image = ImageTk.PhotoImage(header_tl_image)
        header_tl_image_label = Label(self.root, image = self.header_tl_photo_image)
        header_tl_image_label.place(x = 0, y = 0, width = int(screen_width / 3), height = 130)

        # header image top center

        header_tc_image = Image.open("project_images/img_frs.png")
        header_tc_image = header_tc_image.resize((int(screen_width / 3), 130), Image.ANTIALIAS)
        self.header_tc_photo_img = ImageTk.PhotoImage(header_tc_image)
        header_tc_image_label = Label(self.root, image = self.header_tc_photo_img)
        header_tc_image_label.place(x = int(screen_width / 3), y = 0, width = int(screen_width / 3), height = 130)

        # header image top right

        header_tr_image = Image.open("project_images/img_university.jpg")
        header_tr_image = header_tr_image.resize((int(screen_width / 3), 130), Image.ANTIALIAS)
        self.header_tr_photo_image = ImageTk.PhotoImage(header_tr_image)
        header_tr_image_label = Label(self.root, image = self.header_tr_photo_image)
        header_tr_image_label.place(x = 2 * int(screen_width / 3), y = 0, width = int(screen_width / 3), height = 130)

        # body background image

        bg_body_image = Image.open("project_images/img_bg_body.jpg")
        bg_body_image = bg_body_image.resize((1536, 710), Image.ANTIALIAS)
        self.bg_body_photo_image = ImageTk.PhotoImage(bg_body_image)
        bg_body_image_label = Label(self.root, image = self.bg_body_photo_image)
        bg_body_image_label.place(x = 0, y = 130, width = int(screen_width), height = 710)

        # title below header

        title_label = Label(bg_body_image_label, text = "Attendance Management System",
                            font = ("Times New Roman", 35, "bold"), background = "black", foreground = "cyan")
        title_label.place(x = 0, y = 0, width = int(screen_width), height = 65)

        # student details section

        student_details_image = Image.open("project_images/img_student_details.png")
        student_details_image = student_details_image.resize((200, 200), Image.ANTIALIAS)
        self.student_details_photo_image = ImageTk.PhotoImage(student_details_image)
        # student details photo image label
        student_details_image_label = Label(bg_body_image_label, image = self.student_details_photo_image)
        student_details_image_label.place(x = 200, y = 100, width = 200, height = 200)
        # student details page redirecting button
        student_details_button = Button(bg_body_image_label, text = "Student Details", cursor = "hand2",
                                        font = ("Times New Roman", 15, "bold"), background = "teal",
                                        foreground = "white",
                                        command = self.goto_student_details)
        student_details_button.place(x = 200, y = 300, width = 200, height = 40)

        # detect face section

        detect_face_image = Image.open("project_images/img_detect_face.jpeg")
        detect_face_image = detect_face_image.resize((200, 200), Image.ANTIALIAS)
        self.detect_face_photo_image = ImageTk.PhotoImage(detect_face_image)
        # face detection photo image label
        detect_face_image_label = Label(bg_body_image_label, image = self.detect_face_photo_image)
        detect_face_image_label.place(x = 500, y = 100, width = 200, height = 200)
        # face detection page redirecting button
        detect_face_button = Button(bg_body_image_label, text = "Detect Face", cursor = "hand2",
                                    font = ("Times New Roman", 15, "bold"), background = "teal", foreground = "white",
                                    command = self.goto_detect_face)
        detect_face_button.place(x = 500, y = 300, width = 200, height = 40)

        # admin attendance management section

        attendance_management_image = Image.open("project_images/img_admin_attendance.jpg")
        attendance_management_image = attendance_management_image.resize((200, 200), Image.ANTIALIAS)
        self.attendance_management_photo_image = ImageTk.PhotoImage(attendance_management_image)
        # management attendance photo image label
        attendance_management_image_label = Label(bg_body_image_label, image = self.attendance_management_photo_image)
        attendance_management_image_label.place(x = 800, y = 100, width = 200, height = 200)
        # attendance management page redirecting button
        attendance_management_button = Button(bg_body_image_label, text = "Update Attendance", cursor = "hand2",
                                              font = ("Times New Roman", 15, "bold"), background = "teal",
                                              foreground = "white", command = self.goto_attendance_management)
        attendance_management_button.place(x = 800, y = 300, width = 200, height = 40)

        # train facial data section
        train_face_data_image = Image.open("project_images/img_train_fd.jpg")
        train_face_data_image = train_face_data_image.resize((200, 200), Image.ANTIALIAS)
        self.train_face_data_photo_image = ImageTk.PhotoImage(train_face_data_image)
        # train face data photo image label
        train_face_data_image_label = Label(bg_body_image_label, image = self.train_face_data_photo_image)
        train_face_data_image_label.place(x = 1100, y = 100, width = 200, height = 200)
        # train facial data page redirecting button
        train_face_data_button = Button(bg_body_image_label, text = "Train Face Data", cursor = "hand2",
                                        font = ("Times New Roman", 15, "bold"), background = "teal",
                                        foreground = "white", command = self.goto_train_fd)
        train_face_data_button.place(x = 1100, y = 300, width = 200, height = 40)

        # logout section
        logout_image = Image.open("project_images/img_logout.png")
        logout_image = logout_image.resize((200, 200), Image.ANTIALIAS)
        self.logout_photo_image = ImageTk.PhotoImage(logout_image)
        # logout photo label
        logout_image_label = Label(bg_body_image_label, image = self.logout_photo_image)
        logout_image_label.place(x = 650, y = 400, width = 200, height = 200)
        # logout page redirecting button
        logout_button = Button(bg_body_image_label, text = "Logout", cursor = "hand2",
                               font = ("Times New Roman", 15, "bold"), background = "aquamarine",
                               foreground = "black")
        logout_button.place(x = 650, y = 600, width = 200, height = 40)

    # function definitions
    def goto_student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def goto_train_fd(self):
        self.new_window = Toplevel(self.root)
        self.app = TrainFaceData(self.new_window)

    def goto_detect_face(self):
        self.new_window = Toplevel(self.root)
        self.app = DetectFace(self.new_window)

    def goto_attendance_management(self):
        self.new_window = Toplevel(self.root)
        self.app = AttendanceManager(self.new_window)


if __name__ == '__main__':
    winTk = Tk()
    obj = AttendanceSystem(winTk)
    parent_open = True


    def on_closing():
        close = messagebox.askyesno("Close", "Are you sure you want to exit the System ?")
        if close:
            winTk.destroy()


    if parent_open:
        winTk.protocol("WM_DELETE_WINDOW", on_closing)
    winTk.mainloop()

# logout functionality pending
