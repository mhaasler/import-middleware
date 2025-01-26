use common::DataHandler;

pub struct CsvHandler;

impl DataHandler for CsvHandler {
    fn validate(&self, data: &str) -> Result<(), String> {
        // Beispiel-Validierung: Daten dürfen nicht leer sein
        if data.trim().is_empty() {
            return Err("Data is empty".to_string());
        }
        Ok(())
    }

    fn store(&self, data: &str) -> Result<(), String> {
        // Beispiel: Speichern der Daten in die Datenbank
        println!("Storing CSV data: {}", data);
        // Hier kann die MongoDB- oder SQLite-Logik integriert werden
        Ok(())
    }

    fn process(&self, data: &str) -> Result<(), String> {
        // Beispiel: Optionale Verarbeitungsschritte
        println!("Processing CSV data: {}", data);
        Ok(())
    }
}
