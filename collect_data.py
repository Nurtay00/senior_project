import time
from zmqRemoteApi import RemoteAPIClient
from tabulate import tabulate
import os

client = RemoteAPIClient()
sim = client.getObject('sim')
client.setStepping(True)
sim.startSimulation()


table =[]
headers=['time',
         'PosLHipYaw','VelLHipYaw','ForLHipYaw',
         'PosLHipPitch','VelLHipPitch','ForLHipPitch',
         'PosLHipRoll','VelLHipRoll','ForLHipRoll',
         'PosLKnee','VelLKnee','ForLKnee',
         'PosLAnklePitch','VelLAnklePitch','ForLAnklePitch',
         'PosLAnkleRoll','VelLAnkleRoll','ForLAnkleRoll',
         'PosRHipYaw','VelRHipYaw','ForRHipYaw',
         'PosRHipPitch','VelRHipPitch','ForRHipPitch',
         'PosRHipRoll','VelRHipRoll','ForRHipRoll',
         'PosRKnee','VelRKnee','ForRKnee',
         'PosRAnklePitch','VelRAnklePitch','ForRAnklePitch',
         'PosRAnkleRoll','VelRAnkleRoll','ForRAnkleRoll']

while (t := sim.getSimulationTime()) < 3:
    # Left leg
    LHipYaw=sim.getObject("/LHipYaw")
    PosLHipYaw=sim.getJointPosition(LHipYaw)
    VelLHipYaw=sim.getJointVelocity(LHipYaw)
    ForLHipYaw=sim.getJointForce(LHipYaw)

    LHipPitch=sim.getObject("/LHipPitch")
    PosLHipPitch=sim.getJointPosition(LHipPitch)
    VelLHipPitch=sim.getJointVelocity(LHipPitch)
    ForLHipPitch=sim.getJointForce(LHipPitch)

    LHipRoll=sim.getObject("/LHipRoll")
    PosLHipRoll=sim.getJointPosition(LHipRoll)
    VelLHipRoll=sim.getJointVelocity(LHipRoll)
    ForLHipRoll=sim.getJointForce(LHipRoll)

    LKnee=sim.getObject("/LKnee")
    PosLKnee=sim.getJointPosition(LKnee)
    VelLKnee=sim.getJointVelocity(LKnee)
    ForLKnee=sim.getJointForce(LKnee)

    LAnklePitch=sim.getObject("/LAnklePitch")
    PosLAnklePitch=sim.getJointPosition(LAnklePitch)
    VelLAnklePitch=sim.getJointVelocity(LAnklePitch)
    ForLAnklePitch=sim.getJointForce(LAnklePitch)

    LAnkleRoll=sim.getObject("/LAnkleRoll")
    PosLAnkleRoll=sim.getJointPosition(LAnkleRoll)
    VelLAnkleRoll=sim.getJointVelocity(LAnkleRoll)
    ForLAnkleRoll=sim.getJointForce(LAnkleRoll)

    # Right leg
    RHipYaw=sim.getObject("/RHipYaw")
    PosRHipYaw=sim.getJointPosition(RHipYaw)
    VelRHipYaw=sim.getJointVelocity(RHipYaw)
    ForRHipYaw=sim.getJointForce(RHipYaw)

    RHipPitch=sim.getObject("/RHipPitch")
    PosRHipPitch=sim.getJointPosition(RHipPitch)
    VelRHipPitch=sim.getJointVelocity(RHipPitch)
    ForRHipPitch=sim.getJointForce(RHipPitch)

    RHipRoll=sim.getObject("/RHipRoll")
    PosRHipRoll=sim.getJointPosition(RHipRoll)
    VelRHipRoll=sim.getJointVelocity(RHipRoll)
    ForRHipRoll=sim.getJointForce(RHipRoll)

    RKnee=sim.getObject("/RKnee")
    PosRKnee=sim.getJointPosition(RKnee)
    VelRKnee=sim.getJointVelocity(RKnee)
    ForRKnee=sim.getJointForce(RKnee)

    RAnklePitch=sim.getObject("/RAnklePitch")
    PosRAnklePitch=sim.getJointPosition(RAnklePitch)
    VelRAnklePitch=sim.getJointVelocity(RAnklePitch)
    ForRAnklePitch=sim.getJointForce(RAnklePitch)


    RAnkleRoll=sim.getObject("/LAnkleRoll")
    PosRAnkleRoll=sim.getJointPosition(RAnkleRoll)
    VelRAnkleRoll=sim.getJointVelocity(RAnkleRoll)
    ForRAnkleRoll=sim.getJointForce(RAnkleRoll)

    table.append([t,
                  PosLHipYaw,VelLHipYaw,ForLHipYaw,
                  PosLHipPitch,VelLHipPitch,ForLHipPitch,
                  PosLHipRoll,VelLHipRoll,ForLHipRoll,
                  PosLKnee,VelLKnee,ForLKnee,
                  PosLAnklePitch,VelLAnklePitch,ForLAnklePitch,
                  PosLAnkleRoll,VelLAnkleRoll,ForLAnkleRoll,
                  PosRHipYaw,VelRHipYaw,ForRHipYaw,
                  PosRHipPitch,VelRHipPitch,ForRHipPitch,
                  PosRHipRoll,VelRHipRoll,ForRHipRoll,
                  PosRKnee,VelRKnee,ForRKnee,
                  PosRAnklePitch,VelRAnklePitch,ForRAnklePitch,
                  PosRAnkleRoll,VelRAnkleRoll,ForRAnkleRoll
                  ])
   
    client.step()
number_of_files = len([name for name in os.listdir('./Data')])
with open('Data/data'+str(number_of_files)+'.txt', 'w') as f:
    f.write(tabulate(table,headers))
print(table,headers)
sim.stopSimulation()