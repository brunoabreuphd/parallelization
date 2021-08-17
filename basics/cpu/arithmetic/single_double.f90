!!!!
!! File: single_double.f90
!! Description: Timings of arithmetic calculations for single/double precision.
!! Author: Bruno R. de Abreu  |  babreu at illinois dot edu
!! National Center for Supercomputing Applications (NCSA)
!!  
!! Creation Date: Wednesday, 2nd June 2021, 11:26:25 am
!! Last Modified: Thursday, 3rd June 2021, 6:56:37 am
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


program single_vs_double
use, intrinsic :: iso_fortran_env
implicit none

! definition of kinds
integer, parameter :: sp = REAL32 ! single precision
integer, parameter :: dp = REAL64 ! double precision
integer, parameter :: i32 = INT32 ! 32-bit int
integer, parameter :: i64 = INT64 ! 64-bit int

! single precision variables
integer(i32), parameter :: n=1000000000_i32
integer(i32) :: i
real(sp) :: a, b

! double precision variables
integer(i64), parameter :: nn=1000000000_i64
integer(i64) :: ii
real(dp) :: aa, bb

! timing
real(dp) :: startT, endT, execT
 

! single precision loops
write(*,*) 'SINGLE PRECISION TIMINGS'
a = 1.0_sp
b = 1.0_sp
call cpu_time(startT)
101 do i=0_i32, n
	a = a + b
enddo
call cpu_time(endT)
execT = (endT - startT)
write(*,*) 'Addition loop took ', execT, ' s, or ', execT/n, ' s per operation.'
a = 1.0_sp
b = 1.0_sp
call cpu_time(startT)
102 do i=0_i32, n
	a = a * b
enddo
call cpu_time(endT)
execT = (endT - startT)
write(*,*) 'Multiplication loop took ', execT, ' s, or ', execT/n, ' s per operation.'
a = 1.0_sp
b = 1.0_sp
call cpu_time(startT)
103 do i=0_i32, n
	a = a / b
enddo
call cpu_time(endT)
execT = (endT - startT)
write(*,*) 'Division loop took ', execT, ' s, or ', execT/n, ' s per operation.'


! double precision loops
write(*,*)
write(*,*) 'DOUBLE PRECISION TIMINGS'
aa = 1.0_dp
bb = 1.0_dp
call cpu_time(startT)
201 do ii=0_i64, nn
	aa = aa + bb
enddo
call cpu_time(endT)
execT = (endT - startT)
write(*,*) 'Addition loop took ', execT, ' s, or ', execT/n, ' s per operation.'
aa = 1.0_dp
bb = 1.0_dp
call cpu_time(startT)
202 do ii=0_i64, nn
	aa = aa * bb
enddo
call cpu_time(endT)
execT = (endT - startT)
write(*,*) 'Multiplication loop took ', execT, ' s, or ', execT/n, ' s per operation.'
aa = 1.0_dp
bb = 1.0_dp
call cpu_time(startT)
203 do ii=0_i64, nn
	aa = aa / bb
enddo
call cpu_time(endT)
execT = (endT - startT)
write(*,*) 'Division loop took ', execT, ' s, or ', execT/n, ' s per operation.'

end program single_vs_double
