!!!!
!! File: matrix.f90
!! Description: 
!! Author: Bruno R. de Abreu  |  babreu at illinois dot edu
!! National Center for Supercomputing Applications (NCSA)
!!  
!! Creation Date: Wednesday, 2nd June 2021, 4:01:23 pm
!! Last Modified: Thursday, 3rd June 2021, 7:13:26 am
!!  
!! Copyright (c) 2021, Bruno R. de Abreu, National Center for Supercomputing Applications.
!! All rights reserved.
!! License: This program and the accompanying materials are made available to any individual
!!          under the citation condition that follows: On the event that the software is
!!          used to generate data that is used implicitly or explicitly for research
!!          purposes, proper acknowledgment must be provided in the citations section of
!!          publications. This includes both the author's name and the National Center
!!          for Supercomputing Applications. If you are uncertain about how to do
!!          so, please check this page: https://github.com/babreu-ncsa/cite-me.
!!          This software cannot be used for commercial purposes in any way whatsoever.
!!          Omitting this license when redistributing the code is strongly disencouraged.
!!          The software is provided without warranty of any kind. In no event shall the
!!          author or copyright holders be liable for any kind of claim in connection to
!!          the software and its usage.
!!!!


program vector_timing
    use, intrinsic :: iso_fortran_env
    implicit none
    integer, parameter :: dp = REAL64 ! double precision
    integer, parameter :: i64 = INT64 ! 64-bit int
    integer(i64), parameter :: n=10000_i64
    real(dp) :: startT, endT, execT
    real(dp), parameter :: w = 1.0_dp
    real(dp) :: r
    real(dp), dimension(n,n) :: m
    integer(i64) :: i, j

    !! ROW MAJOR: i-j loop
    write(*,*) 'ROW MAJOR: i-j loop'
    !! write
    call cpu_time(startT)
    do i = 1, n
        do j = 1, n
            m(i,j) = w
        enddo
    enddo
    call cpu_time(endT)    
    execT = (endT - startT)
    write(*,*) 'Writing to matrix time ', execT, ' s, or ', execT/(n*n), ' s per operation.' 
    !! read
    call cpu_time(startT)
    do i = 1, n
        do j = 1, n
            r = m(i,j)
        enddo
    enddo
    call cpu_time(endT)    
    execT = (endT - startT)
    write(*,*) 'Reading from matrix time ', execT, ' s, or ', execT/(n*n), ' s per operation.' 

    !! COLUMN MAJOR: j-i loop
    write(*,*)
    write(*,*) 'COLUMN MAJOR: j-i loop'
    !! write
    call cpu_time(startT)
    do j = 1, n
        do i = 1, n
            m(i,j) = w
        enddo
    enddo
    call cpu_time(endT)    
    execT = (endT - startT)
    write(*,*) 'Writing to matrix time ', execT, ' s, or ', execT/(n*n), ' s per operation.' 
    !! read
    call cpu_time(startT)
    do j = 1, n
        do i = 1, n
            r = m(i,j)
        enddo
    enddo
    call cpu_time(endT)    
    execT = (endT - startT)
    write(*,*) 'Reading from matrix time ', execT, ' s, or ', execT/(n*n), ' s per operation.'    

end program 