import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import math
import openpyxl
import os.path
from common_libs import scan_excel
from kiot_features import nhap_hang, refresh, hthi_thong_tin_sp, xuat_hang
from kiot_features import tinh_tong_tien_nhap


def GUI_Nhap_SP(file_path, window, row_ref, column_ref):
    style = ttk.Style()
    style.configure('My.TLabelframe', background='orange', padding=0)

    style_noshadow = ttk.Style()
    style_noshadow.configure('NoShadow.TLabelframe', relief='flat', borderwidth=10)

    group_box = ttk.LabelFrame(window, text="Lấy Hàng", style='NoShadow.TLabelframe')
    group_box.grid(row=row_ref+0, column=column_ref+1, padx=5, pady=5)

    # Set the desired size for Group 1
    group_box.config(width=390, height=280)
    group_box.grid_propagate(False)  # Disable size propagation

    # Nhập tên mặt hàng
    ten_hang_hoa = ttk.Label(group_box, text="Thêm tên mặt hàng:")
    ten_hang_hoa.grid(row=row_ref+0, column=column_ref+0, padx=10, pady=10, sticky="e")
    # tạo ô nhập tên
    ten_hang_hoa_entry = ttk.Entry(group_box)
    ten_hang_hoa_entry.grid(row=row_ref+0, column=column_ref+1, padx=10, pady=10, sticky="e")

    # Nhập mã cho hàng hóa
    ma_hang_hoa = ttk.Label(group_box, text="Thêm mã hàng:")
    ma_hang_hoa.grid(row=row_ref+1, column=column_ref+0, padx=10, pady=10, sticky="e")
    # tạo ô nhập mã hàng hóa
    ma_hang_hoa_entry = ttk.Entry(group_box)
    ma_hang_hoa_entry.grid(row=row_ref+1, column=column_ref+1, padx=10, pady=10, sticky="e")

    # Nhập giá lấy vào
    gia_tien = ttk.Label(group_box, text="Thêm giá nhập/1SP:")
    gia_tien.grid(row=row_ref+2, column=column_ref+0, padx=10, pady=10, sticky="e")
    # tạo ô nhập giá
    gia_tien_nhap_entry = ttk.Entry(group_box)
    gia_tien_nhap_entry.grid(row=row_ref+2, column=column_ref+1, padx=10, pady=10, sticky="e")

    # Hiển thị số đơn vị tien te
    don_vi_label_sp_0 = ttk.Label(group_box, text="Nghìn VND")
    don_vi_label_sp_0.grid(row=row_ref+2, column=column_ref+2, padx=10, pady=10, sticky="e")

    # Nhập số lượng lấy vào
    so_luong = ttk.Label(group_box, text="Thêm số lượng nhập:")
    so_luong.grid(row=row_ref+3, column=column_ref+0, padx=10, pady=10, sticky="e")
    # tạo ô nhập số lượng
    so_luong_nhap_entry = ttk.Entry(group_box)
    so_luong_nhap_entry.grid(row=row_ref+3, column=column_ref+1, padx=10, pady=10, sticky="e")

    # Nhập giá bán
    gia_ban_1sp = ttk.Label(group_box, text="Thêm giá bán/1SP:")
    gia_ban_1sp.grid(row=row_ref+4, column=column_ref+0, padx=10, pady=10, sticky="e")
    # tạo ô nhập giá bán
    gia_ban_1sp_entry = ttk.Entry(group_box)
    gia_ban_1sp_entry.grid(row=row_ref+4, column=column_ref+1, padx=10, pady=10, sticky="e")

    # Hiển thị số đơn vị tien te
    don_vi_label_sp_1 = ttk.Label(group_box, text="Nghìn VND")
    don_vi_label_sp_1.grid(row=row_ref+4, column=column_ref+2, padx=10, pady=10, sticky="e")

    # tạo nút nhập để hoàn thành thao tác
    save_button = ttk.Button(
    group_box,
    text="Hoàn thành nhập",
    command=lambda: nhap_hang(file_path,
        ten_hang_hoa_entry,
        ma_hang_hoa_entry,
        gia_tien_nhap_entry,
        so_luong_nhap_entry,
        gia_ban_1sp_entry
    )
    )
    save_button.grid(row=row_ref+5, column=column_ref+1, padx=10, pady=10)

def GUI_Xuat_Kho(file_path, window, row_ref, column_ref):
    style_noshadow = ttk.Style()
    style_noshadow.configure('NoShadow.TLabelframe', relief='flat', borderwidth=10)
    xk_group_box = ttk.LabelFrame(window, text="Cập nhật bán ra", style='NoShadow.TLabelframe')
    xk_group_box.grid(row=row_ref+0, column=column_ref+1, padx=5, pady=5, sticky=tk.W)

    # Set the desired size for Group 1
    xk_group_box.config(width=390, height=190)
    xk_group_box.grid_propagate(False)  # Disable size propagation

    # Nhập tên mặt hàng
    xk_ten_hang_hoa = ttk.Label(xk_group_box, text="Thêm tên mặt hàng đã bán:")
    xk_ten_hang_hoa.grid(row=row_ref+0, column=column_ref+0, padx=10, pady=10, sticky="e")
    # tạo ô nhập tên
    xk_ten_hang_hoa_entry = ttk.Entry(xk_group_box)
    xk_ten_hang_hoa_entry.grid(row=row_ref+0, column=column_ref+1, padx=10, pady=10, sticky="e")

    # Nhập mã cho hàng hóa
    xk_ma_hang_hoa = ttk.Label(xk_group_box, text="Thêm mã hàng đã bán:")
    xk_ma_hang_hoa.grid(row=row_ref+1, column=column_ref+0, padx=10, pady=10, sticky="e")
    # tạo ô nhập mã hàng hóa
    xk_ma_hang_hoa_entry = ttk.Entry(xk_group_box)
    xk_ma_hang_hoa_entry.grid(row=row_ref+1, column=column_ref+1, padx=10, pady=10, sticky="e")

    # Nhập số lượng lấy vào
    xk_so_luong = ttk.Label(xk_group_box, text="Thêm số lượng bán ra:")
    xk_so_luong.grid(row=row_ref+3, column=column_ref+0, padx=10, pady=10, sticky="e")
    # tạo ô nhập số lượng
    xk_so_luong_ban_ra_entry = ttk.Entry(xk_group_box)
    xk_so_luong_ban_ra_entry.grid(row=row_ref+3, column=column_ref+1, padx=10, pady=10, sticky="e")

    # tạo nút nhập để hoàn thành thao tác
    xk_button = ttk.Button(
    xk_group_box,
    text="Hoàn thành xuất kho",
    command=lambda: xuat_hang(file_path,
        xk_ten_hang_hoa_entry,
        xk_ma_hang_hoa_entry,
        xk_so_luong_ban_ra_entry
    )
    )
    xk_button.grid(row=row_ref+5, column=column_ref+1, columnspan=2, padx=10, pady=10)

def GUI_Ktra_TTSP(file_path, window, 
                                row_ref, column_ref):
    style_noshadow = ttk.Style()
    style_noshadow.configure('NoShadow.TLabelframe', relief='flat', borderwidth=10)
    thong_tin_ten_sp, thong_tin_ma_sp, thong_tin_gia_sp, thong_tin_sl_sp = scan_excel(file_path)
    check_group_box = ttk.LabelFrame(window, text="Kiểm tra thông tin sản phẩm", style='NoShadow.TLabelframe')
    check_group_box.grid(row=row_ref+0, column=column_ref+1, padx=5, pady=5, sticky=tk.N)

    # Set the desired size for Group 1
    check_group_box.config(width=790, height=190)
    check_group_box.grid_propagate(False)  # Disable size propagation

    # Theo tên sản phẩm
    param1_label = ttk.Label(check_group_box, text="Kiểm tra theo tên SP:")
    param1_label.grid(row=row_ref+0, column=column_ref+0, padx=10, pady=10)

    param1_combobox = ttk.Combobox(check_group_box, values=thong_tin_ten_sp)
    param1_combobox.grid(row=row_ref+0, column=column_ref+1, padx=10, pady=10)

    # Hiển thị giá bán
    gia_ban_label = ttk.Label(check_group_box, text="Giá bán/1SP:")
    gia_ban_label.grid(row=row_ref+0, column=column_ref+2, padx=10, pady=10)

    gia_ban_display = ttk.Label(check_group_box, text="####")
    gia_ban_display.grid(row=row_ref+0, column=column_ref+3,padx=10, pady=10)

    # Hiển thị số đơn vị tiền tệ
    don_vi_label = ttk.Label(check_group_box, text="Nghìn VND")
    don_vi_label.grid(row=row_ref+0, column=column_ref+4, padx=10, pady=10)

    # Hiển thị số lượng nhập
    sl_nhap_label = ttk.Label(check_group_box, text="Số lượng nhập:")
    sl_nhap_label.grid(row=row_ref+0, column=column_ref+5, padx=10, pady=10)

    sl_nhap_display = ttk.Label(check_group_box, text="####")
    sl_nhap_display.grid(row=row_ref+0, column=column_ref+6,padx=10, pady=10)

    # Hiển thị số đơn vị sp
    don_vi_label_sp = ttk.Label(check_group_box, text="SP")
    don_vi_label_sp.grid(row=row_ref+0, column=column_ref+7, padx=10, pady=10)

    # Hiển thị số lượng còn lại
    sl_con_lai_label = ttk.Label(check_group_box, text="Số lượng tồn kho:")
    sl_con_lai_label.grid(row=row_ref+1, column=column_ref+2, padx=10, pady=10)

    sl_con_lai_display = ttk.Label(check_group_box, text="####")
    sl_con_lai_display.grid(row=row_ref+1, column=column_ref+3,padx=10, pady=10)

    # Hiển thị số đơn vị sp
    don_vi_label_sp_0 = ttk.Label(check_group_box, text="SP")
    don_vi_label_sp_0.grid(row=row_ref+1, column=column_ref+4, padx=10, pady=10)

    # Hiển thị số lượng đã bán ra
    sl_ban_ra_label = ttk.Label(check_group_box, text="Số lượng đã bán ra:")
    sl_ban_ra_label.grid(row=row_ref+1, column=column_ref+5, padx=10, pady=10)

    sl_ban_ra_display = ttk.Label(check_group_box, text="####")
    sl_ban_ra_display.grid(row=row_ref+1, column=column_ref+6,padx=10, pady=10)

    # Hiển thị số đơn vị sp
    don_vi_label_sp_1 = ttk.Label(check_group_box, text="SP")
    don_vi_label_sp_1.grid(row=row_ref+1, column=column_ref+7, padx=10, pady=10)

    # Theo mã sản phẩm
    param2_label = ttk.Label(check_group_box, text="Kiểm tra theo mã SP:")
    param2_label.grid(row=row_ref+1, column=column_ref+0, padx=10, pady=10)

    param2_combobox = ttk.Combobox(check_group_box, values=thong_tin_ma_sp)
    param2_combobox.grid(row=row_ref+1, column=column_ref+1, padx=10, pady=10)

    # Create the parameter selection comboboxes

    # Create the Refresh button
    refresh_button = ttk.Button(check_group_box, 
    text="Refresh", 
    command=lambda: refresh(param1_combobox, 
                            param2_combobox,
                            file_path
                            )
    )
    refresh_button.grid(row=row_ref+5, column=column_ref+0, padx=10, pady=10, sticky=tk.N)

    # Create the kiểm tra button
    ktra_button = ttk.Button(check_group_box, 
    text="Kiểm tra", 
    command=lambda: hthi_thong_tin_sp(file_path,
                            param1_combobox, 
                            param2_combobox,
                            gia_ban_display,
                            sl_nhap_display,
                            sl_ban_ra_display,
                            sl_con_lai_display
                            )
    )
    ktra_button.grid(row=row_ref+5, column=column_ref+1, padx=10, pady=10)

def GUI_Tinh_Excel(file_path, window, row_ref, column_ref):
    style_noshadow = ttk.Style()
    style_noshadow.configure('NoShadow.TLabelframe', relief='flat', borderwidth=10)
    thong_ke_group_box = ttk.LabelFrame(window, text="Thống kê bán hàng", style='NoShadow.TLabelframe')
    thong_ke_group_box.grid(row=row_ref+1, column=column_ref+1, padx=5, pady=5, sticky=tk.W)

    # Set the desired size for Group 1
    thong_ke_group_box.config(width=390, height=150)
    thong_ke_group_box.grid_propagate(False)  # Disable size propagation

    # Hiển thị số tiền nhập hàng hàng tháng
    tien_nhap_hang_label = ttk.Label(thong_ke_group_box, text="Tổng tiền nhập/tháng:")
    tien_nhap_hang_label.grid(row=row_ref+1, column=column_ref+1, padx=10, pady=10, sticky="e")

    tien_nhap_hang_display = ttk.Label(thong_ke_group_box, text="####")
    tien_nhap_hang_display.grid(row=row_ref+1, column=column_ref+2,padx=10, pady=10, sticky="e")

    # Hiển thị số đơn vị tiền tệ
    don_vi_label_0 = ttk.Label(thong_ke_group_box, text="Nghìn VND")
    don_vi_label_0.grid(row=row_ref+1, column=column_ref+3, padx=10, pady=10, sticky="e")

    # Hiển thị số tiền bán được hàng hàng tháng
    doanh_thu_hang_label = ttk.Label(thong_ke_group_box, text="Tổng doanh thu/tháng:")
    doanh_thu_hang_label.grid(row=row_ref+2, column=column_ref+1, padx=10, pady=10, sticky="e")

    doanh_thu_hang_display = ttk.Label(thong_ke_group_box, text="####")
    doanh_thu_hang_display.grid(row=row_ref+2, column=column_ref+2,padx=10, pady=10, sticky="e")

    # Hiển thị số đơn vị tiền tệ
    don_vi_label_1 = ttk.Label(thong_ke_group_box, text="Nghìn VND")
    don_vi_label_1.grid(row=row_ref+2, column=column_ref+3, padx=10, pady=10, sticky="e")

    # Create the Refresh button
    show_button = ttk.Button(thong_ke_group_box, 
    text="Thống kê", 
    command=lambda: tinh_tong_tien_nhap(file_path, tien_nhap_hang_display, doanh_thu_hang_display)
    )
    show_button.grid(row=row_ref+3, column=column_ref+1, columnspan=2, padx=10, pady=10)

def GUI_Sign(window, row_ref, column_ref):
    sign = ttk.Style()
    sign.configure('sign.TLabelframe', relief='flat', borderwidth=10)
    # Create a custom font with the Harlow Solid Italic font
    font_name = "Chiller"
    custom_font = Font(family=font_name, size=14, slant="italic")
    xk_group_box = ttk.LabelFrame(window, text="Designed by", style='sign.TLabelframe')
    xk_group_box.grid(row=row_ref+0, column=column_ref+1, padx=5, pady=15, sticky="se")

    # Set the desired size for Group 1
    xk_group_box.config(width=120, height=50)
    xk_group_box.grid_propagate(False)  # Disable size propagation

    # tạo chữ ký
    ky_ten_label = ttk.Label(xk_group_box, text="Chú Chuột Típ", font=custom_font)
    ky_ten_label.grid(row=row_ref+0, column=column_ref+0, padx=0, pady=0, sticky="e")



    