from opcua import Client
import time
import struct
import math
import socket
from scipy.spatial.transform import Rotation as R

url = "opc.tcp://192.168.10.239:4840"

client = Client(url)

# user name / pw
userName = "zhaw"
password = "zhawzhawzhaw"
client.set_user(userName)
client.set_password(password)
client.connect()
print("client Panda connected . . .")
# node id


SERVER = "192.168.10.171"
PORT = 5001
ADDR = (SERVER, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
print("Client Pickit connected . . .")

while True:
    # cartesianPose ns=2;i=7020
    Pos = client.get_node("ns=2;i=7020")
    Position = Pos.get_value()
    print(f' The catresian Pose is: {Position}')
    # print(Position)
    print("--------------------------------------------------------------------")


    MULT = 10000
    A = int((Position[3][0] * MULT))
    print(f' The Position X  is: {A}')
    #print(A)
    B = int((Position[3][1] * MULT))
    print(f' The Position Y  is: {B}')
    #print(B)
    C = int((Position[3][2] * MULT))
    print(f' The Position Z  is: {C}')
    #print(C)

    position_X = (A).to_bytes(4, byteorder='big',signed=True)
    position_Y = (B).to_bytes(4, byteorder='big',signed=True)
    position_Z = (C).to_bytes(4, byteorder='big',signed=True)

    print(f' The Byte Position X  is: {position_X}')
    print(f' The len of Position X  is: {len(position_X)}')
    #print(position_X)
    #print(len(position_X))
    print(f' The Byte Position Y  is: {position_Y}')
    print(f' The len of Position Y  is: {len(position_Y)}')
    #print(position_Y)
    #print(len(position_Y))
    print(f' The Byte Position Z  is: {position_Z}')
    print(f' The len of Position Z  is: {len(position_Z)}')
    #print(position_Z)
    #print(len(position_Z))


    # Position only need = [3][0] [3][1] [3][2]
    position_byte_list = [position_X,position_Y,position_Z]
    final_position_bytes = b''.join(position_byte_list)
    print(f'The final position bytes: {final_position_bytes}')
    #print(final_position_bytes)
    print(f'The len of final position bytes: {len(final_position_bytes)}')
    print(len(final_position_bytes))
    print("--------------------------------------------------------------------")
########################################## Orientation #################################################
    r = R.from_matrix([ [Position[0][0], Position[0][1], Position[0][2]] , [Position[1][0], Position[1][1], Position[1][2]] , [Position[2][0], Position[2][1], Position[2][2]]])

    orientation = r.as_quat()
    print(orientation)
    q0 = int((orientation[0] * MULT))
    q1 = int((orientation[1] * MULT))
    q2 = int((orientation[2] * MULT))
    q3 = int((orientation[3] * MULT))
    print(f'The orientation Q0 is: {q0}')
    print(f'The orientation Q1 is: {q1}')
    print(f'The orientation Q2 is: {q2}')
    print(f'The orientation Q3 is: {q3}')


    final_q0 = (q0).to_bytes(4, byteorder='big',signed=True)
    final_q1 = (q1).to_bytes(4, byteorder='big',signed=True)
    final_q2 = (q2).to_bytes(4, byteorder='big',signed=True)
    final_q3 = (q3).to_bytes(4, byteorder='big',signed=True)
    byte_list = [final_q0,final_q1,final_q2,final_q3]
    final_orientation = b''.join(byte_list)


    #final_orientation = final_q0 + final_q1 + final_q2 + final_q3
    print(f"The orientation bytes are : {final_q0} // {final_q1} // {final_q2} // {final_q3}")
    print(f'The final orientation byte is : {final_orientation}')
    print(f'The len of final orientation byte is : {len(final_orientation)}')
    print("--------------------------------------------------------------------")



    ############################################## command ##############################################


    RC_PICKIT_CHECK_MODE = 0
    RC_PICKIT_NO_COMMAND = -1
    RC_PICKIT_SHUTDOWN_SYSTEM = 2
    RC_PICKIT_FIND_CALIB_PLATE = 10
    RC_PICKIT_CONFIGURE_CALIB = 11
    RC_PICKIT_COMPUTE_CALIB = 12
    RC_PICKIT_VALIDATE_CALIB = 13
    RC_PICKIT_LOOK_FOR_OBJECTS = 20
    RC_PICKIT_LOOK_FOR_OBJECTS_WITH_RETRIES = 21
    RC_PICKIT_CAPTURE_IMAGE = 22
    RC_PICKIT_PROCESS_IMAGE = 23
    RC_PICKIT_NEXT_OBJECT = 30
    RC_PICKIT_CONFIGURE = 40
    RC_PICKIT_SET_CYLINDER_DIM = 41
    RC_SAVE_ACTIVE_SETUP = 42
    RC_SAVE_ACTIVE_PRODUCT = 43
    RC_PICKIT_SAVE_SCENE = 50
    RC_PICKIT_BUILD_BACKGROUND = 60
    RC_PICKIT_GET_PICK_POINT_DATA = 70

    byte_RC_PICKIT_CHECK_MODE = (RC_PICKIT_CHECK_MODE).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_NO_COMMAND = (RC_PICKIT_NO_COMMAND).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_SHUTDOWN_SYSTEM = (RC_PICKIT_SHUTDOWN_SYSTEM).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_FIND_CALIB_PLATE = (RC_PICKIT_FIND_CALIB_PLATE).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_CONFIGURE_CALIB = (RC_PICKIT_CONFIGURE_CALIB).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_COMPUTE_CALIB = (RC_PICKIT_COMPUTE_CALIB).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_VALIDATE_CALIB = (RC_PICKIT_VALIDATE_CALIB).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_LOOK_FOR_OBJECTS = (RC_PICKIT_LOOK_FOR_OBJECTS).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_LOOK_FOR_OBJECTS_WITH_RETRIES = (RC_PICKIT_LOOK_FOR_OBJECTS_WITH_RETRIES).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_CAPTURE_IMAGE = (RC_PICKIT_CAPTURE_IMAGE).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_PROCESS_IMAGE = (RC_PICKIT_PROCESS_IMAGE).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_NEXT_OBJECT = (RC_PICKIT_NEXT_OBJECT).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_CONFIGURE = (RC_PICKIT_CONFIGURE).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_SET_CYLINDER_DIM = (RC_PICKIT_SET_CYLINDER_DIM).to_bytes(4, byteorder='big', signed=True)
    byte_RC_SAVE_ACTIVE_SETUP = (RC_SAVE_ACTIVE_SETUP).to_bytes(4, byteorder='big', signed=True)
    byte_RC_SAVE_ACTIVE_PRODUCT = (RC_SAVE_ACTIVE_PRODUCT).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_SAVE_SCENE = (RC_PICKIT_SAVE_SCENE).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_BUILD_BACKGROUND = (RC_PICKIT_BUILD_BACKGROUND).to_bytes(4, byteorder='big', signed=True)
    byte_RC_PICKIT_GET_PICK_POINT_DATA = (RC_PICKIT_GET_PICK_POINT_DATA).to_bytes(4, byteorder='big', signed=True)

    print(f' The chekc mode byte is : {byte_RC_PICKIT_CHECK_MODE}')
    print("----------------------------------------------------------------------")

    ################# payload ########################3

    Payload = 0
    Payload2 = 0
    byte_payload = (Payload).to_bytes(4, byteorder='big',signed=True)
    byte_payload2 = (Payload2).to_bytes(4, byteorder='big',signed=True)
    payload_byte_list = [byte_payload,byte_payload2]
    final_payload = b''.join(payload_byte_list)

    print(f"The payload byte are : {final_payload} ")
    print(f' The len of payload byte is {len(final_payload)}')
    print("----------------------------------------------------------------------")

    ########################### mata data #################################3
    # 2 and 11
    meta1 = 2
    meta2 = 11
    byte_meta1 = (meta1).to_bytes(4, byteorder='big',signed=True)
    byte_meta2 = (meta2).to_bytes(4, byteorder='big',signed=True)
    print(f" meta data 1 :  {byte_meta1}")
    print(f" meta data 2 :  {byte_meta2}")
    print("----------------------------------------------------------------------")

    # Final state
    # position 12 B , orientation 16 B, command = 4 B, payload = 8 B, meta = 8 B
    final_byte_list = [final_position_bytes,final_orientation,byte_RC_PICKIT_CHECK_MODE,final_payload,byte_meta1,byte_meta2]
    final_check_mode = b''.join(final_byte_list)

    # byte_RC_PICKIT_GET_PICK_POINT_DATA
    final_byte_list_get_data = [final_position_bytes,final_orientation,byte_RC_PICKIT_CAPTURE_IMAGE,final_payload,byte_meta1,byte_meta2]
    final_get_data_mode = b''.join(final_byte_list_get_data)

    print(f"The final bytes of check mode are: {final_check_mode} ")
    print(f"The len of final bytes of check mode are: {final_check_mode} ")
    print("----------------------------------------------------------------------")



    s.send(final_check_mode)
    print("Sent")


    msg = s.recv(1024)  # output is bytes
    print(" Received")
    if (len(msg)) <= 0:
        print(" No response. . .")
    else:
        print(" Response message: ")
        print(msg)
        print("----------------------------------------------------------------------")

    x = msg
    byte_position = x[:12]  # 12 -3
    byte_position_x = x[:4]
    byte_position_y = x[4:8]
    byte_position_z = x[8:12]

    byte_orientation = x[12:28]  # 16 - 4
    byte_orientation_a = x[12:16]
    byte_orientation_b = x[16:20]
    byte_orientation_c = x[20:24]
    byte_orientation_d = x[24:28]

    byte_payload = x[28:52]  # 24 - 6
    byte_payload_1 = x[28:32]
    byte_payload_2 = x[32:36]
    byte_payload_3 = x[36:40]
    byte_payload_4 = x[40:44]
    byte_payload_5 = x[44:48]
    byte_payload_6 = x[48:52]

    byte_status = x[52:56]  # 4 - 1

    byte_meta = x[56:64]  # 8 - 2
    byte_meta_1 = x[56:60]
    byte_meta_2 = x[60:64]

    position = int.from_bytes(byte_position, byteorder='big', signed=True)
    position_x = int.from_bytes(byte_position_x, byteorder='big', signed=True)
    position_y = int.from_bytes(byte_position_y, byteorder='big', signed=True)
    position_z = int.from_bytes(byte_position_z, byteorder='big', signed=True)

    orientation = int.from_bytes(byte_orientation, byteorder='big', signed=True)
    orientation_a = int.from_bytes(byte_orientation_a, byteorder='big', signed=True)
    orientation_b = int.from_bytes(byte_orientation_b, byteorder='big', signed=True)
    orientation_c = int.from_bytes(byte_orientation_c, byteorder='big', signed=True)
    orientation_d = int.from_bytes(byte_orientation_d, byteorder='big', signed=True)

    payload = int.from_bytes(byte_payload, byteorder='big', signed=True)
    payload_1 = int.from_bytes(byte_payload_1, byteorder='big', signed=True)
    payload_2 = int.from_bytes(byte_payload_2, byteorder='big', signed=True)
    payload_3 = int.from_bytes(byte_payload_3, byteorder='big', signed=True)
    payload_4 = int.from_bytes(byte_payload_4, byteorder='big', signed=True)
    payload_5 = int.from_bytes(byte_payload_5, byteorder='big', signed=True)
    payload_6 = int.from_bytes(byte_payload_6, byteorder='big', signed=True)

    status = int.from_bytes(byte_status, byteorder='big', signed=True)

    meta = int.from_bytes(byte_meta, byteorder='big', signed=True)
    meta_1 = int.from_bytes(byte_meta_1, byteorder='big', signed=True)
    meta_2 = int.from_bytes(byte_meta_2, byteorder='big', signed=True)

    print(f'The position x is: {position_x}')
    print(f'The position y is: {position_y}')
    print(f'The position z is: {position_z}')
    print("----------------------------------------------------------------------")

    print(f' The orientation a is: {orientation_a}')
    print(f' The orientation b is: {orientation_b}')
    print(f' The orientation c is: {orientation_c}')
    print(f' The orientation d is: {orientation_d}')

    print("----------------------------------------------------------------------")
    print(f' The payload 1 is: {payload_1}')
    print(f' The payload 2 is: {payload_2}')
    print(f' The payload 3 is: {payload_3}')
    print(f' The payload 4 is: {payload_4}')
    print(f' The payload 5 is: {payload_5}')
    print(f' The payload 6 is: {payload_6}')

    print("----------------------------------------------------------------------")
    print(f' The status is: {status}')
    print("----------------------------------------------------------------------")
    print(f' The meta 1 is: {meta_1}')
    print(f' The meta 2 is: {meta_2}')








