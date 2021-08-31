!!!!
!! File: dotprod_openmp.f90
!! Description: Simple OpenMP implementation of a dot product between two vectors 
!! Author: Bruno R. de Abreu  |  babreu at illinois dot edu
!! National Center for Supercomputing Applications (NCSA)
!!  
!! Creation Date: Tuesday, 31st August 2021, 10:04:25 am
!! Last Modified: Tuesday, 31st August 2021, 12:09:15 pm
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

program dotproduct
    use, intrinsic :: iso_fortran_env
    use :: omp_lib
    implicit none
    integer, parameter :: dp = REAL64 ! double precision
    integer, parameter :: i32 = INT32 ! 32-bit int
    integer(i32), parameter :: ord=100000000_i32
    real(dp) :: startT, endT
    real(dp), dimension(:), allocatable :: x, y
    real(dp) :: dotp

    ! allocate
    allocate(x(ord))
    allocate(y(ord))
    ! initial random values
    call random_seed()
    call random_number(x)
    call random_number(y)

    ! call and time routine
    startT = omp_get_wtime()
    call dotprod(ord,x,y,dotp)
    endT = omp_get_wtime()

    ! print outputs
    write(*,*) 'Dot product = ', dotp
    write(*,*) 'Time (s) = ', (endT-startT)

    ! free
    deallocate(x)
    deallocate(y)

end program dotproduct    


subroutine dotprod(ord,x,y,dotp)
    !! calculates dot product
    use, intrinsic :: iso_fortran_env
    use :: omp_lib
    implicit none
    integer, parameter :: dp = REAL64 ! double precision
    integer, parameter :: i32 = INT32 ! 32-bit int
    integer(i32), intent(in) :: ord
    real(dp), dimension(ord), intent(in) :: x, y
    real(dp), intent(out) :: dotp
    integer(i32) :: i

    dotp = 0.0_dp
    !$omp parallel do reduction(+:dotp)    
    do i = 1, ord
        dotp = dotp + x(i)*y(i)
    enddo
    !$omp end parallel do
    
end subroutine dotprod
