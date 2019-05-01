import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Router } from '@angular/router' 

@Injectable()
export class AuthService {

    constructor(private http: HttpClient, private router: Router) {

    }

    get isAuthenticated() {
        return !!localStorage.getItem('token')
    }

    register(credentials) {
        console.log(credentials)
        this.http.post<any>(`http://localhost:8000/api/users/`, credentials).subscribe(res => {
            console.log(res);
            this.authenticate(res);
        })
    }

    login(credentials) {
        this.http.post<any>(`http://localhost:8000/api-auth/login/`, credentials).subscribe(res => {
            console.log(res);
            this.authenticate(res);
        })
    }

    authenticate(res) {
        localStorage.setItem('token', res);

        this.router.navigate(['/'])
    }

    logout() {
        localStorage.removeItem('token');
    }
}