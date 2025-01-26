// Placeholder for the common module

pub fn common_info() -> &'static str {
    "Common module is working!"
}

pub trait DataHandler {
    fn validate(&self, data: &str) -> Result<(), String>;
    fn store(&self, data: &str) -> Result<(), String>;
    fn process(&self, data: &str) -> Result<(), String>;
}