import { Component } from '@angular/core'
import { FormBuilder, Validators } from '@angular/forms'
import { AuthService } from '../services/auth-service/auth.service'

@Component ({
    templateUrl: './register.component.html',
    styleUrls: ['./register.component.css']
})
export class RegisterComponent {

    form

    constructor(private auth: AuthService, private fb: FormBuilder) {
        this.form = fb.group({
            username: ['', Validators.required],
            password: ['', Validators.required],
            email : ['', Validators.pattern('^([a-zA-Z0-9-.]+)@([a-zA-Z0-9-.]+).([a-zA-Z]{2,5})$')]
        })
    }
}