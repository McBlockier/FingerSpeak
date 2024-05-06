package com.fingerspeak;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckedTextView;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class LoginActivity extends AppCompatActivity {

    private EditText editTextUsername;
    private EditText editTextPassword;
    private Button btnLogin;
    private CheckedTextView createAccut;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_login);

        getComponents(); //Método para obtener los componentes
        linkEvents(); //Método para ligar eventos a los componentes

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.login), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }

    private void getComponents(){

        btnLogin = findViewById(R.id.btnLogin); //Obtenemos el boton de login
        editTextUsername = findViewById(R.id.userName); //Obtenemos el campo de Username
        editTextPassword = findViewById(R.id.password); //Obtenemos el campo de Password
        createAccut = findViewById(R.id.checkCreate); //Obtenemos el campo de crear Cuenta
    }

    private void linkEvents(){
        // Configurar un escuchador de clics para el botón de inicio de sesión
        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Llamar al método onClickLogin cuando se hace clic en el botón
                validateLogin();
            }
        });


    }

    private void validateLogin(){
        String username = editTextUsername.getText().toString();
        String password = editTextPassword.getText().toString();

        if(!username.isEmpty() && !password.isEmpty()){


       }else{
            if (username.isEmpty()) {
                Toast.makeText(this, "Por favor, ingresa tu usuario", Toast.LENGTH_SHORT).show();
            } else if (password.isEmpty()) {
                Toast.makeText(this, "Por favor, ingresa tu contraseña", Toast.LENGTH_SHORT).show();
            }
        }


    }
}

