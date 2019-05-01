import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Subject } from 'rxjs'
@Injectable()
export class ApiService {

    constructor(private http: HttpClient) {

    }

    getAllRestaurants() {
        return this.http.get('https://localhost:8000/api/restaurants');
    }
}