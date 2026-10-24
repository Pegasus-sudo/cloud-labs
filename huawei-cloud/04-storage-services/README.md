# Storage Services on Huawei Cloud: EVS, OBS and SFS Turbo

> Hands-on lab covering the three core storage types on Huawei Cloud: block storage (EVS), object storage (OBS) and shared file storage (SFS Turbo).

**Platform:** Huawei Cloud
**Source:** Huawei Cloud HCCDP-Solution Architectures program
**Date completed:** [Month Year]
**Region:** [e.g., AP-Singapore]

## Objective
- Perform EVS practice (block storage attached to servers)
- Perform OBS practice (object storage)
- Perform SFS practice (shared file system)

## Services used
- Elastic Volume Service (EVS)
- Object Storage Service (OBS)
- Scalable File Service Turbo (SFS Turbo)
- Elastic Cloud Server (ECS): Windows and Linux
- Elastic IP (EIP)

## Architecture
![Architecture diagram](architecture/diagram.png)

[One or two lines: which ECS instances were used and how each storage type connects to them.]

## What I did

### 1. EVS (block storage)
- Purchased an EVS disk
- Attached a non-shared EVS disk to a Windows ECS
- Initialized the disk
- Detached the disk and verified the result

### 2. OBS (object storage)
- Created a bucket
- Uploaded, downloaded and deleted a file or folder

### 3. SFS Turbo (shared file storage)
- Bound an EIP to the ECS
- Created an SFS Turbo file system
- Mounted the file system to a Linux ECS
- Installed the NFS client on a Windows ECS and mounted the file system
- Verified access: [what you checked, e.g., a file created from one server visible from the other]

## Verification
![EVS disk attached](screenshots/evs-attached.png)
![OBS bucket](screenshots/obs-bucket.png)
![SFS mounted](screenshots/sfs-mounted.png)

## Key learnings
- **EVS** is block storage attached to a single server, like a virtual hard disk that must be initialized before use.
- **OBS** is object storage accessed through buckets, suited for files, backups and static content.
- **SFS** is a shared file system that multiple servers (Linux and Windows) can mount at the same time over NFS.
- Choosing the right storage type depends on access pattern: single-server disk, shared files, or object storage.

## Cost and cleanup
Resources released after the lab (disks, buckets, file system, EIP): [yes / no].

## Possible improvements
- Add EVS snapshots or backups
- Add OBS lifecycle rules and access policies
- Compare SFS Turbo with other file storage options for performance
