import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Subject, Observable } from 'rxjs'
@Injectable()
export class ApiService {

    constructor(private http: HttpClient) {

    }

    getAllRestaurants() {
        return this.http.get('http://localhost:8000/api/restaurants');
    }

    getAllDishesForRestaurant(){
        return this.http.get(`http://localhost:8000/api/dishes/`);
    }

    getProfile(){
        return this.http.get('http://localhost:8000/api/users/getprofile/');
    }

    updateProfile(profile){
        this.http.put('http://localhost:8000/api/users/updateprofile', profile).subscribe(res => {
            console.log(res);
        })
    }

    deleteDish(dishId): Observable<any>{
        return this.http.delete('http://localhost:8000/api/users/updateprofile', dishId);
    }

    addDish(dish): Observable<any>{
        return this.http.post('http://localhost:8000/api/dishes/adddish', dish);
    }
}
