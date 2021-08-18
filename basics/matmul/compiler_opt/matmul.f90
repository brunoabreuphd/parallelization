!!!!
!! File: matmul.f90
!! Description: Matrix multiplication code
!! Author: Bruno R. de Abreu  |  babreu at illinois dot edu
!! National Center for Supercomputing Applications (NCSA)
!!  
!! Creation Date: Tuesday, 17th August 2021, 9:29:08 am
!! Last Modified: Tuesday, 17th August 2021, 9:29:21 am
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

program matmul
    use, intrinsic :: iso_fortran_env
    implicit none
    integer, parameter :: dp = REAL64 ! double precision
    integer, parameter :: i32 = INT32 ! 32-bit int
    integer(i32), parameter :: ord=1000_i32
    real(dp) :: startT, endT
    real(dp), parameter :: zero=0.0_dp, one=1.0_dp, two=2.0_dp
    real(dp), dimension(ord,ord) :: m, n, p
    integer(i32) :: i, j, k

    !! filling up matrices
    p = zero
    m = one
    n = two

    !! trivial matrix multiplication
    call cpu_time(startT)
    do k = 1, ord
        do j = 1, ord
            do i = 1, ord
                p(i,j) = m(i,k) * n(k,j) 
            enddo
        enddo
    enddo
    call cpu_time(endT)
    write(*,*) 'Matrix multiplication took: ', (endT-startT), ' s'

end program matmul
